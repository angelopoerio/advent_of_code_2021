#!/usr/bin/env python3


def check_matrix(matrix, number):
    for row in matrix:
        for item in row:
            if item["number"] == number:
                item["marked"] = True

    # check the rows
    if all([item["marked"] for row in matrix for item in row]):
        return True

    # check the columns
    for row_index in range(5):
        if all(
            [matrix[column_index][row_index]["marked"] for column_index in range(5)]
        ):
            return True
    return False


def solve(list_of_matrices, numbers):
    for number in numbers:
        for matrix in list_of_matrices:
            if check_matrix(matrix, number):
                return number * sum(
                    [
                        item["number"]
                        for row in matrix
                        for item in row
                        if not item["marked"]
                    ]
                )
    raise Exception("No solution found :|")


if __name__ == "__main__":
    with open("input.txt") as fn:
        lines = fn.readlines()

        numbers = [int(num) for num in lines[0].split(",")]
        matrix = []
        list_of_matrices = []

        for counter, line in enumerate(
            [ln for ln in lines[1:] if not ln.startswith("\n")]
        ):
            matrix.append(
                [
                    {"number": int(num), "marked": False}
                    for num in line.strip().split(" ")
                    if num
                ]
            )
            if (counter + 1) % 5 == 0:
                list_of_matrices.append(matrix)
                matrix = []

        solution = solve(list_of_matrices, numbers)
        print(f"The solution is {solution}")
