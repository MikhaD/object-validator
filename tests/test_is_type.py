"""
>>> import Validate
>>> Validate.is_type(1, int)
True
>>> Validate.is_type([], list)
True
>>> Validate.is_type({1, 2}, set)
True

>>> Validate.is_type(Validate.is_type, tuple)
False
>>> Validate.is_type([1, 1, 1], dict)
False
>>> Validate.is_type([1, 1, 1], set[int])
False

>>> Validate.is_type((1, 1, 1), tuple)
True
>>> Validate.is_type((1, 1, 1), tuple[int])
False
>>> Validate.is_type((1, 1, 1), tuple[int, str, int])
False
>>> Validate.is_type((1, "1", 1), tuple[int, str, int])
True
>>> Validate.is_type((1, "1", (1, "1")), tuple[int, str, tuple[int, str]])
True

>>> Validate.is_type({}, dict)
True
>>> Validate.is_type({1}, dict)
False
>>> Validate.is_type({"a": "", "b": "", "c": "", "d": ""}, dict[str])
True
>>> Validate.is_type({"a": 1, "b": "", "c": "", "d": ""}, dict[str])
False
>>> Validate.is_type({"a": 1, "b": "", "c": "", "d": ""}, dict[str, int])
True
>>> Validate.is_type({"a": 1, "b": {"a": 1}, "c": (5, True), "d": ""}, dict[str, int, dict[int], tuple[bool, bool]])
False
>>> Validate.is_type({"a": 1, "b": {"a": 1}, "c": (5, True), "d": ""}, dict[str, int, dict[int], tuple[int, bool]])
True

>>> Validate.is_type({1, "1"}, set)
True
>>> Validate.is_type({1, "1"}, set[int])
False
>>> Validate.is_type({1, "1"}, set[str, int])
True
>>> Validate.is_type({1, 3}, set[int])
True
>>> Validate.is_type({1, "3", (4, "a")}, set[int, str, tuple])
True
>>> Validate.is_type({1, "3", (4, "a")}, set[int, str, tuple[int, str]])
True

>>> Validate.is_type([1, "1"], list)
True
>>> Validate.is_type([1, "1"], list[int])
False
>>> Validate.is_type([1, "1"], list[str, int])
True
>>> Validate.is_type([1, 3], list[int])
True
>>> Validate.is_type([1, "3", (4, "a")], list[int, str, tuple])
True
>>> Validate.is_type([1, "3", (4, "a")], list[int, str, tuple[int, str]])
True
>>> Validate.is_type([1, "3", (4, "a", {5, 6, True})], list[int, str, tuple[int, str, set]])
True
>>> Validate.is_type([1, "3", (4, "a", {5, 6, True})], list[int, str, tuple[int, str, set[bool]]])
False
>>> Validate.is_type([1, "3", (4, "a", {5, 6, True})], list[int, str, tuple[int, str, set[bool, int]]])
True

>>> Validate.is_type(("hello", 3, [False, 1, True]), tuple[str, int, list[bool]])
False
>>> Validate.is_type(("hello", 3, [False, True, True]), tuple[str, int, list[bool]])
True
"""