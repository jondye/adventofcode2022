#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import ascii_letters


def day3(contents):
    total = 0
    for rucksack in contents:
        first_half = set(rucksack[:len(rucksack)//2])
        second_half = set(rucksack[len(rucksack)//2:])
        common = first_half.intersection(second_half).pop()
        total += ascii_letters.index(common) + 1
    return total


def main():
    with open('input3.txt') as contents:
        print(f"Total of duplicate item priorities is {day3(contents)}")


if __name__ == '__main__':
    main()
