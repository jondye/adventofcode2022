#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import ascii_letters
from itertools import tee


def day3_1(contents):
    return sum(
        priority(common(rucksack.strip()))
        for rucksack in contents)


def common(rucksack):
    first_half = set(rucksack[:len(rucksack)//2])
    second_half = set(rucksack[len(rucksack)//2:])
    return set.intersection(first_half, second_half).pop()


def priority(letter):
    return ascii_letters.index(letter) + 1


def day3_2(contents):
    rucksacks = iter(set(line.strip()) for line in contents)
    return sum(
        priority(badge(group))
        for group in zip(rucksacks, rucksacks, rucksacks))


def badge(group):
    return set.intersection(*group).pop()


def main():
    with open('input3.txt') as contents:
        part1, part2 = tee(contents)
        print(f"Total of duplicate item priorities is {day3_1(part1)}")
        print(f"Total of group badge priorities is {day3_2(part2)}")


if __name__ == '__main__':
    main()
