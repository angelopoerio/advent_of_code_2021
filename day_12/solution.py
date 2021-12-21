#!/usr/bin/env python3

from collections import defaultdict


def solve(map, start, smallCaves=[]):
    cnt = 0

    if start == "end":
        return 1

    for cave in map[start]:
        if not cave.islower() or cave not in smallCaves:
            cnt += solve(map, cave, smallCaves=smallCaves + [cave])
    return cnt


if __name__ == "__main__":
    map = defaultdict(list)
    smallCaves = []

    with open("input.txt") as fn:
        for line in fn.readlines():
            caves = line.strip().split("-")
            map[caves[0]].append(caves[1])
            map[caves[1]].append(caves[0])
        solution = solve(map, "start", smallCaves=smallCaves)
        print(f"The solutions is {solution}")
