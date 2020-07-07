def min_indices_removed(strings: list) -> int:
    rows = len(strings)

    if rows <= 1:
        return 0

    columns = len(strings[0])

    if columns == 0:
        return 0

    removed_indices = 0

    for column in range(columns):
        for row in range(1, rows):
            if strings[row][column] < strings[row - 1][column]:
                removed_indices += 1
                break

    return removed_indices


if __name__ == '__main__':
    strings_n = int(input())
    _ = input()

    strings = list()
    for string_n in range(strings_n):
        strings.append(input())

    print(min_indices_removed(strings))
