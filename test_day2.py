#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2022/day/2
"""

from day2 import day2, score_by_hand

from io import StringIO

from hamcrest import assert_that, contains_exactly, equal_to


strategy = """A Y
B X
C Z
"""


def test_day2():
    file_input = StringIO(strategy)
    assert_that(
        day2(file_input),
        contains_exactly(15, 12))


def test_score_by_hand():
    assert_that(score_by_hand("A X"), equal_to(4))
    assert_that(score_by_hand("A Y"), equal_to(8))
    assert_that(score_by_hand("A Z"), equal_to(3))
    assert_that(score_by_hand("B X"), equal_to(1))
    assert_that(score_by_hand("B Y"), equal_to(5))
    assert_that(score_by_hand("B Z"), equal_to(9))
    assert_that(score_by_hand("C X"), equal_to(7))
    assert_that(score_by_hand("C Y"), equal_to(2))
    assert_that(score_by_hand("C Z"), equal_to(6))
