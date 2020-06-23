from typing import List


def matrix_neighbors(matrix: List[List[int]], row: int, column: int) -> List[int]:
    if len(matrix) == 0:
        return []

    rows = len(matrix)
    columns = len(matrix[0])

    neighbors = list()

    if column > 0:
        neighbors.append(matrix[row][column - 1])

    if column < columns - 1:
        neighbors.append(matrix[row][column + 1])

    if row > 0:
        neighbors.append(matrix[row - 1][column])

    if row < rows - 1:
        neighbors.append(matrix[row + 1][column])

    return sorted(neighbors)


if __name__ == '__main__':
    matrix = list()
    rows = int(input())
    _ = input()

    for _ in range(rows):
        row = [int(n) for n in input().split(" ")]
        matrix.append(row)

    row = int(input())
    column = int(input())

    print(" ".join(str(n) for n in matrix_neighbors(matrix, row, column)))
