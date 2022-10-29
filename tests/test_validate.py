"""
>>> import validate
>>> from typing import Union
>>> validate.validate({"a": 1}, {"a": int})
True
>>> validate.validate({"a": True}, {"a": int})
False
>>> validate.validate({"b": True}, {"a": bool})
False
>>> validate.validate({"b": [True, False]}, {"b": list[bool]})
True
>>> validate.validate({"b": {"c": 3}}, {"b": {"c": int}})
True
>>> validate.validate({"b": {"c": 3, "d": []}}, {"b": {"c": int, "d": list}})
True
>>> validate.validate({"b": {"c": 3, "d": [5, 6]}}, {"b": {"c": int, "d": list[str]}})
False
>>> validate.validate({"b": {"c": 3, "d": [{"f": "hi"}, {"f": "bye"}]}}, {"b": {"c": int, "d": list[str]}})
False
>>> validate.validate({"b": {"c": 3, "d": [{"f": "hi"}, {"f": "bye"}]}}, {"b": {"c": int, "d": [{"f": str}]}})
True
>>> validate.validate({"b": {"c": 3, "d": [{"f": "hi"}, {"d": "bye"}]}}, {"b": {"c": int, "d": [{"f": str}]}})
False
>>> validate.validate({"b": {"c": 3, "d": [{"f": "hi"}, {"d": "bye"}]}}, {"b": {"c": int, "d": [{"f": str},{"d": str}]}})
True
>>> validate.validate({"b": 1, "c": 3}, {"b": int})
False
>>> validate.validate({"b": 1, "c": 3, "d": 5}, {"b": int, str: int})
True
>>> validate.validate({"c": 3, "d": 5}, {"b": int, str: int})
False
>>> validate.validate({"b": {"c": 3, "d": [{"f": "hi"}, {"d": "bye", "f": "oops"}]}}, {"b": {"c": int, "d": [{"f": str},{str: str}]}})
True
>>> validate.validate({"b": {"c": 3, "d": [{"f": "hi"}, {"d": "bye", "f": "oops"}]}}, {"b": {"c": int, "d": [{"f": str},{"d": str}]}})
False
>>> validate.validate({"b": {"c": 3, "d": 4}}, {"b": {"c": int, "d": 5}})
False
>>> validate.validate({"b": {"c": 3, "d": 5}}, {"b": {"c": int, "d": 5}})
True
>>> validate.validate({"b": 1, "c": 3, "d": 3}, {"b": int, str: 3})
True
>>> validate.validate({"b": 1, "c": 3, "d": 5}, {"b": int, str: 3})
False
>>> validate.validate({"c": 3, "d": 3}, {"b": int, str: 3})
False
>>> validate.validate({"b": 3, "c": 3, "d": "3"}, {"b": int, str: Union[int, str]})
True
>>> validate.validate({"b": "3"}, {"b": Union[int, str]})
True
"""