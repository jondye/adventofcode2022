#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2022/day/3
"""

from day3 import day3

from io import StringIO

from hamcrest import assert_that, equal_to


contents = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_day3():
    assert_that(day3(StringIO(contents)), equal_to(157))
