#!/usr/bin/env python
# -*- coding: utf-8 -*-


def day4(contents):
    total = 0
    for assignments in contents:
        a, b = (tuple(map(int, assignment.split('-')))
                for assignment in assignments.strip().split(','))
        if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
            total += 1
    return total


def main():
    with open('input4.txt') as sections:
        print(f"Number of completely overlapping pairs is {day4(sections)}")


if __name__ == '__main__':
    main()
