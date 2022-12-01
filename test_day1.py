#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2022/day/1
"""

from day1 import day1, sum_calories
from hamcrest import assert_that, contains_exactly, equal_to

calorie_list = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_day1():
    assert_that(
        day1(calorie_list.splitlines(True)),
        contains_exactly(24000, 45000))

def test_sum_calories():
    assert_that(
        list(sum_calories(calorie_list.splitlines())),
        contains_exactly(6000, 4000, 11000, 24000, 10000))
