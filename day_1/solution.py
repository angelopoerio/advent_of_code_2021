#!/usr/bin/env python3


def solve(lst_of_depths):
    prev = lst_of_depths[0]
    increases = 0
    for depth in lst_of_depths[1:]:
        if depth > prev:
            increases += 1
        prev = depth
    return increases


if __name__ == "__main__":
    with open("input") as fn:
        lines = [int(ln.strip()) for ln in fn.readlines()]
        print(f"Solution is {solve(lines)}")
