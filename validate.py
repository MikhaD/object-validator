from types import GenericAlias, UnionType
from typing import Any, Union, _UnionGenericAlias  # type: ignore

class InvalidSchema(Exception):
	"""Raised when a schema is invalid."""
	pass

def is_type(value: Any, test_type: Union[type, GenericAlias, UnionType]):
	"""
	Check if a value is of a certain type or parameterized generic type. Returns `True` if the value is of the given type, and `False` otherwise. Type can be any primitive python type, `int`, `float`, `bool`, or `str`, or any of the raw basic data structures, `list`, `tuple`, `dict`, or `set`.

	The main use for this function comes from its support for parameterized generic types. For example, `is_type([1, 2, 3], list[int])` returns `True`, and `is_type([1, 2, 3], list[str])` returns `False`. This is useful for validating lists of objects, for example.
	"""
	if type(value) == test_type: return True
	if type(test_type) in (_UnionGenericAlias, UnionType):
		types = getattr(test_type, "__args__", None)
		for t in types:
			if is_type(value, t): return True
		return False
	if type(value) not in (tuple, set, list, dict): return False
	base_type = getattr(test_type, "__origin__", False)
	type_args = getattr(test_type, "__args__", [])
	if not base_type or type(value) != base_type: return False
	if base_type == tuple:
		if len(type_args) != len(value): return False
		for v, t in zip(value, getattr(test_type, "__args__")):
			if not is_type(v, t): return False
		return True
	if base_type == dict:
		for v in value.values():
			for t in type_args:
				if is_type(v, t): break
			else: return False
		return True
	# if base_type == list or base_type == set:
	for v in value:
		for t in type_args:
			if is_type(v, t): break
		# for else triggers the else if the for loop ends without breaking
		else: return False
	return True

def validate(obj: Any, schema: Any):
	"""
	Check if a dict or list matches a schema.
	"""
	if isinstance(schema, (int, float, str, bool)) or schema is None:
		return obj == schema
	if isinstance(schema, (type, GenericAlias, UnionType, _UnionGenericAlias)):
		return is_type(obj, schema)
	if type(obj) != type(schema):
		return False
	if type(schema) == dict:
		non_literals = 0
		general_key = False
		for key in schema:
			if isinstance(key, str):
				if key not in obj: return False
				if not validate(obj[key], schema[key]): return False
			elif key == str:
				if general_key: raise InvalidSchema("Multiple general keys in schema")
				general_key = True
				for k in obj:
					if k not in schema:
						if not validate(obj[k], schema[key]): return False
						non_literals += 1
		# True is the same as 1, False is the same as 0
		if len(obj) - non_literals != len(schema) - general_key: return False

	elif type(schema) == list:
		for i in obj:
			for sub_schema in schema:
				if validate(i, sub_schema):
					break
			# for else triggers the else if the for loop ends without breaking
			else: return False
	return True