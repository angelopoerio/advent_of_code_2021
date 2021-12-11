#!/usr/bin/env python3


def solve(positions):
    min_position = min(positions)
    max_position = max(positions)
    min_fuel = 10 ** 6

    for aligned_position in range(min_position, max_position):
        used_fuel = 0
        used_fuel += sum(abs(aligned_position - position) for position in positions)

        if used_fuel < min_fuel:
            min_fuel = used_fuel

    return min_fuel


if __name__ == "__main__":
    with open("input.txt") as fn:
        positions = [int(position) for position in fn.readline().strip().split(",")]
        print(f"The solution is {solve(positions)}")
