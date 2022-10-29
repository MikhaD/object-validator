# Validate JSON
![min version](https://img.shields.io/static/v1?label=python&message=v10.0%2B&color=3776ab&logo=python)

A simple tool to validate python dictionaries and/or lists against a schema. I was working on a different project that couldn't use 3rd party libraries and needed to work with JSON files provided by the user, so I wrote this tool to check that a given object matches a given schema.

This project is comprised of two functions, `is_type` and `validate`.
## Usage
This is not a comprehensive json validator. What follows are instructions on how to write a valid schema and how to use the validator.
### `is_type`
`is_type` takes two arguments, a value and a type. It returns `True` if the value is of the given type, and `False` otherwise. Type can be any primitive python type, `int`, `float`, `bool`, or `str`, or any of the raw basic data structures, `list`, `tuple`, `dict`, or `set`.
However, for these types you might as well use the `type` function. The real power of `is_type` is that it supports parameterized generic types. For example, `is_type([1, 2, 3], list[int])` returns `True`, and `is_type([1, 2, 3], list[str])` returns `False`. This is useful for validating lists of objects, for example.

Types can be as deeply nested as you like. For example, the type list[tuple[int, str], dict[bool, str], int] matches a list that can contain tuples of integers and strings, dictionaries with values that are booleans or strings, or integers.
### `validate`
`validate` uses `is_type` and takes two arguments, an object and a schema. It returns `True` if the object matches the schema, and `False` otherwise. An object in this context is a python dictionary or list. The result produced by `json.parse` is the perfect candidate for this function.
Because of the way `validate` uses `is_type`, it can be used in place of `is_type` without any change in functionality.
## Schema Syntax
- The schema is a python dictionary or list.
- In a dictionary keys in the schema must be in the object.
INCOMPLETE