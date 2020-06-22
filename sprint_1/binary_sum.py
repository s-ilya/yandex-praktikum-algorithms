def binary_sum(left: str, right: str) -> str:
    left_numbers = [int(digit) for digit in left]
    right_numbers = [int(digit) for digit in right]

    left_index = len(left_numbers) - 1
    right_index = len(right_numbers) - 1
    carried_digit = 0
    result = list()

    while left_index >= 0 and right_index >= 0:
        carried_digit, sum = divmod(left_numbers[left_index] + right_numbers[right_index] + carried_digit, 2)
        result.append(sum)
        left_index -= 1
        right_index -= 1

    while left_index >= 0:
        carried_digit, sum = divmod(left_numbers[left_index] + carried_digit, 2)
        result.append(sum)
        left_index -= 1

    while right_index >= 0:
        carried_digit, sum = divmod(right_numbers[right_index] + carried_digit, 2)

        result.append(sum)
        right_index -= 1

    if carried_digit != 0:
        result.append(carried_digit)

    return "".join([str(digit) for digit in reversed(result)])


if __name__ == '__main__':
    print(binary_sum(input(), input()))
