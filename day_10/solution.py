#!/usr/bin/env python3


def compute_score(line):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    matching_symbols = {"[": "]", "{": "}", "<": ">", "(": ")"}
    closing = []
    for symbol in line:
        if symbol in ["[", "{", "(", "<"]:
            closing.append(symbol)
        else:
            popped_symbol = closing.pop()
            if matching_symbols[popped_symbol] != symbol:
                return scores[symbol]
    return 0


if __name__ == "__main__":
    with open("input.txt") as fn:
        total_score = 0
        for line in fn.readlines():
            total_score += compute_score(line.strip())
        print(f"Total score is {total_score}")
