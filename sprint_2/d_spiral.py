def spiral(matrix: list) -> list:
    if len(matrix) == 0:
        return []

    result = list()

    start_row = 0
    start_column = 0
    end_row = len(matrix)
    end_column = len(matrix[0])

    while start_row < end_row and start_column < end_column:
        for column_index in range(start_column, end_column):
            result.append(matrix[start_row][column_index])

        for row_index in range(start_row + 1, end_row):
            result.append(matrix[row_index][end_column - 1])

        if (end_row - 1) != start_row:
            for column_index in range(end_column - 2, start_column, -1):
                result.append(matrix[end_row - 1][column_index])

        if (end_column - 1) != start_column:
            for row_index in range(end_row - 1, start_row, -1):
                result.append(matrix[row_index][start_column])

        start_column += 1
        start_row += 1
        end_column -= 1
        end_row -= 1

    return result


if __name__ == '__main__':
    rows_n = int(input())
    columns_n = int(input())

    matrix = list()

    for _ in range(rows_n):
        matrix.append([int(n) for n in input().split(' ')])

    for n in spiral(matrix):
        print(n)
