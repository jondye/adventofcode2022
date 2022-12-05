#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2022/day/3
"""

from day3 import day3_1, day3_2

from io import StringIO

from hamcrest import assert_that, equal_to


contents = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_day3_1():
    assert_that(day3_1(StringIO(contents)), equal_to(157))


def test_day3_2():
    assert_that(day3_2(StringIO(contents)), equal_to(70))
