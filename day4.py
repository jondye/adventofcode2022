#!/usr/bin/env python
# -*- coding: utf-8 -*-


def day4(contents):
    ranges = [[
        tuple(map(int, assignment.split('-')))
        for assignment in assignments.strip().split(',')]
        for assignments in contents]
    print("\n".join(f"{r} {partial_overlap(*r)}" for r in ranges))
    return (
        sum(complete_overlap(*x) for x in ranges),
        sum(partial_overlap(*x) for x in ranges))


def complete_overlap(a, b):
    return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])


def partial_overlap(a, b):
    return (a[0] <= b[1] and a[1] >= b[0])


def main():
    with open('input4.txt') as sections:
        part1, part2 = day4(sections)
        print(f"Number of completely overlapping pairs is {part1}")
        print(f"Number of partially overlapping pairs is {part2}")


if __name__ == '__main__':
    main()
