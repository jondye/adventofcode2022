#!/usr/bin/env python
# -*- coding: utf-8 -*-

def day2(strategy):
    return sum(score(round.strip()) for round in strategy)


def score(hand):
    lookup = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    return lookup[hand]


def main():
    with open('input2.txt') as strategy:
        print(f"Total score according to strategy is {day2(strategy)}")


if __name__ == '__main__':
    main()
