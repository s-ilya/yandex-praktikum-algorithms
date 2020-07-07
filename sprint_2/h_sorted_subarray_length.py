def max_sorted_sub_length(arr: list) -> int:
    if len(arr) <= 1:
        return len(arr)

    max_length = 1
    current_length = 1
    for index in range(len(arr) - 1):
        if arr[index] < arr[index + 1]:
            current_length += 1
        else:
            max_length = max_length if max_length > current_length else current_length
            current_length = 1

    return max_length if max_length > current_length else current_length


if __name__ == '__main__':
    _ = input()

    print(
        max_sorted_sub_length(
            [int(n) for n in input().split(' ')]
        )
    )
