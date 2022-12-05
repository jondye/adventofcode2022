#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://adventofcode.com/2022/day/2
"""

from day2 import day2, score

from io import StringIO

from hamcrest import assert_that, equal_to
import pytest


strategy = """A Y
B X
C Z
"""


def test_day2():
    file_input = StringIO(strategy)
    assert_that(day2(file_input), equal_to(15))


def test_score():
    assert_that(score("A X"), equal_to(4))
    assert_that(score("A Y"), equal_to(8))
    assert_that(score("A Z"), equal_to(3))
    assert_that(score("B X"), equal_to(1))
    assert_that(score("B Y"), equal_to(5))
    assert_that(score("B Z"), equal_to(9))
    assert_that(score("C X"), equal_to(7))
    assert_that(score("C Y"), equal_to(2))
    assert_that(score("C Z"), equal_to(6))