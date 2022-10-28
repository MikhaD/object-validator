"""
>>> import Validate
>>> Validate.validate_schema({"a": 1}, {"a": int})
True
>>> Validate.validate_schema({"a": True}, {"a": int})
False
>>> Validate.validate_schema({"b": True}, {"a": bool})
False
>>> Validate.validate_schema({"b": [True, False]}, {"b": list[bool]})
True
>>> Validate.validate_schema({"b": {"c": 3}}, {"b": {"c": int}})
True
>>> Validate.validate_schema({"b": {"c": 3, "d": []}}, {"b": {"c": int, "d": list}})
True
>>> Validate.validate_schema({"b": {"c": 3, "d": [5, 6]}}, {"b": {"c": int, "d": list[str]}})
False
>>> Validate.validate_schema({"b": {"c": 3, "d": [{"f": "hi"}, {"f": "bye"}]}}, {"b": {"c": int, "d": list[str]}})
False
>>> Validate.validate_schema({"b": {"c": 3, "d": [{"f": "hi"}, {"f": "bye"}]}}, {"b": {"c": int, "d": [{"f": str}]}})
True
>>> Validate.validate_schema({"b": {"c": 3, "d": [{"f": "hi"}, {"d": "bye"}]}}, {"b": {"c": int, "d": [{"f": str}]}})
False
>>> Validate.validate_schema({"b": {"c": 3, "d": [{"f": "hi"}, {"d": "bye"}]}}, {"b": {"c": int, "d": [{"f": str},{"d": str}]}})
True
>>> Validate.validate_schema({"b": 1, "c": 3}, {"b": int})
False
>>> Validate.validate_schema({"b": 1, "c": 3, "d": 5}, {"b": int, str: int})
True
>>> Validate.validate_schema({"c": 3, "d": 5}, {"b": int, str: int})
False
>>> Validate.validate_schema({"b": {"c": 3, "d": [{"f": "hi"}, {"d": "bye", "f": "oops"}]}}, {"b": {"c": int, "d": [{"f": str},{str: str}]}})
True
>>> Validate.validate_schema({"b": {"c": 3, "d": [{"f": "hi"}, {"d": "bye", "f": "oops"}]}}, {"b": {"c": int, "d": [{"f": str},{"d": str}]}})
False
>>> Validate.validate_schema({"b": {"c": 3, "d": 4}}, {"b": {"c": int, "d": 5}})
False
>>> Validate.validate_schema({"b": {"c": 3, "d": 5}}, {"b": {"c": int, "d": 5}})
True
>>> Validate.validate_schema({"b": 1, "c": 3, "d": 3}, {"b": int, str: 3})
True
>>> Validate.validate_schema({"b": 1, "c": 3, "d": 5}, {"b": int, str: 3})
False
>>> Validate.validate_schema({"c": 3, "d": 3}, {"b": int, str: 3})
False
"""