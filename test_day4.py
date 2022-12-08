#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2022/day/4
"""

from day4 import day4

from io import StringIO

from hamcrest import assert_that, contains_exactly


ranges = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_day4():
    assert_that(day4(StringIO(ranges)), contains_exactly(2, 4))
