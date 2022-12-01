#!/usr/bin/env python
# -*- coding: utf-8 -*-

def day1_1(calorie_list):
    per_elf_calories = sum_calories(val.strip() for val in calorie_list)
    return max(per_elf_calories)

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
        print(f"The most calories held by an elf is {day1_1(calorie_list)}")

if __name__ == '__main__':
    main()