#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import tee


def day2(strategy):
    a, b = tee(round.strip() for round in strategy)
    return (
        sum(score_by_hand(val) for val in a),
        sum(score_by_outcome(val) for val in b)
    )


def score_by_hand(hand):
    """Assumes X=Rock, Y=Paper, Z=Scissors"""
    lookup = {
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }
    return lookup[hand]


def score_by_outcome(hand):
    """Assumes X=Lose, Y=Draw, Z=Win"""
    lookup = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6,
    }
    return lookup[hand]


def main():
    with open('input2.txt') as strategy:
        part1, part2 = day2(strategy)
        print(f"Total score according to hand strategy is {part1}")
        print(f"Total score according to outcome strategy is {part2}")


if __name__ == '__main__':
    main()
