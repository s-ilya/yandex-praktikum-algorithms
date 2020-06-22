from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    if len(matrix) == 0:
        return []

    original_rows_len = len(matrix)
    original_columns_len = len(matrix[0])

    result = list()
    for original_column_idx in range(original_columns_len):
        row = list()
        result.append(row)

        for original_row_idx in range(original_rows_len):
            row.append(matrix[original_row_idx][original_column_idx])

    return result


if __name__ == '__main__':
    rows_count = int(input())
    _ = input()

    matrix = list()
    for _ in range(rows_count):
        row = list([int(n) for n in input().split(" ")])
        matrix.append(row)

    transposed = transpose(matrix)
    for row in transposed:
        print(" ".join([str(n) for n in row]))
