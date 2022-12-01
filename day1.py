#!/usr/bin/env python
# -*- coding: utf-8 -*-

def day1(calorie_list):
    per_elf_calories = sum_calories(val.strip() for val in calorie_list)
    per_elf_calories = sorted(per_elf_calories)
    return (per_elf_calories[-1], sum(per_elf_calories[-3:]))


def sum_calories(calorie_list):
    total = 0
    for val in calorie_list:
        if val:
            total += int(val)
        else:
            yield total
            total = 0
    yield total


def main():
    with open('input1.txt') as calorie_list:
        top_elf, top_three_elves = day1(calorie_list)
    print(f"The most calories held by an elf is {top_elf}")
    print(f"The top three Elves are carrying {top_three_elves} calories")


if __name__ == '__main__':
    main()
