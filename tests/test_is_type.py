"""
>>> from typing import Union
>>> import validate
>>> validate.is_type(1, int)
True
>>> validate.is_type([], list)
True
>>> validate.is_type({1, 2}, set)
True

>>> validate.is_type(4, Union[int, str])
True
>>> validate.is_type("4", Union[int, str])
True
>>> validate.is_type(4.0, Union[int, str])
False
>>> validate.is_type("4", int | str)
True
>>> validate.is_type(4, int | str)
True
>>> validate.is_type(4.0, int | str)
False

>>> validate.is_type(validate.is_type, tuple)
False
>>> validate.is_type([1, 1, 1], dict)
False
>>> validate.is_type([1, 1, 1], set[int])
False

>>> validate.is_type((1, 1, 1), tuple)
True
>>> validate.is_type((1, 1, 1), tuple[int])
False
>>> validate.is_type((1, 1, 1), tuple[int, str, int])
False
>>> validate.is_type((1, "1", 1), tuple[int, str, int])
True
>>> validate.is_type((1, "1", (1, "1")), tuple[int, str, tuple[int, str]])
True

>>> validate.is_type({}, dict)
True
>>> validate.is_type({1}, dict)
False
>>> validate.is_type({"a": "", "b": "", "c": "", "d": ""}, dict[str])
True
>>> validate.is_type({"a": 1, "b": "", "c": "", "d": ""}, dict[str])
False
>>> validate.is_type({"a": 1, "b": "", "c": "", "d": ""}, dict[str, int])
True
>>> validate.is_type({"a": 1, "b": {"a": 1}, "c": (5, True), "d": ""}, dict[str, int, dict[int], tuple[bool, bool]])
False
>>> validate.is_type({"a": 1, "b": {"a": 1}, "c": (5, True), "d": ""}, dict[str, int, dict[int], tuple[int, bool]])
True

>>> validate.is_type({1, "1"}, set)
True
>>> validate.is_type({1, "1"}, set[int])
False
>>> validate.is_type({1, "1"}, set[str, int])
True
>>> validate.is_type({1, 3}, set[int])
True
>>> validate.is_type({1, "3", (4, "a")}, set[int, str, tuple])
True
>>> validate.is_type({1, "3", (4, "a")}, set[int, str, tuple[int, str]])
True

>>> validate.is_type([1, "1"], list)
True
>>> validate.is_type([1, "1"], list[int])
False
>>> validate.is_type([1, "1"], list[str, int])
True
>>> validate.is_type([1, 3], list[int])
True
>>> validate.is_type([1, "3", (4, "a")], list[int, str, tuple])
True
>>> validate.is_type([1, "3", (4, "a")], list[int, str, tuple[int, str]])
True
>>> validate.is_type([1, "3", (4, "a", {5, 6, True})], list[int, str, tuple[int, str, set]])
True
>>> validate.is_type([1, "3", (4, "a", {5, 6, True})], list[int, str, tuple[int, str, set[bool]]])
False
>>> validate.is_type([1, "3", (4, "a", {5, 6, True})], list[int, str, tuple[int, str, set[bool, int]]])
True

>>> validate.is_type(("hello", 3, [False, 1, True]), tuple[str, int, list[bool]])
False
>>> validate.is_type(("hello", 3, [False, True, True]), tuple[str, int, list[bool]])
True

>>> validate.is_type(["hello", 3, [False, True, True]], list[str | int, list])
True
>>> validate.is_type(["hello", 3, [False, True, True]], list[str | int | list])
True
>>> validate.is_type([1, True, 4, ["hi", 5]], list[int | bool | list[str]])
False
>>> validate.is_type([1, True, 4, ["hi", 5]], list[int | bool | list[str | int]])
True
>>> validate.is_type([1, 4, ["hi", 5]], list[int | bool | list])
True
"""