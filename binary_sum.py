from collections import deque


def binary_sum(left: str, right: str) -> str:
    left_numbers = list(map(int, left))
    right_numbers = list(map(int, right))

    left_index = len(left_numbers) - 1
    right_index = len(right_numbers) - 1
    carried_digit = 0
    result = deque()

    while left_index >= 0 and right_index >= 0:
        sum_carried_tuple = sum_digits(left_numbers[left_index],
                                       right_numbers[right_index],
                                       carried_digit)

        result.appendleft(sum_carried_tuple[0])
        carried_digit = sum_carried_tuple[1]
        left_index -= 1
        right_index -= 1

    while left_index >= 0:
        sum_carried_tuple = sum_digits(left_numbers[left_index], 0,
                                       carried_digit)

        result.appendleft(sum_carried_tuple[0])
        carried_digit = sum_carried_tuple[1]
        left_index -= 1

    while right_index >= 0:
        sum_carried_tuple = sum_digits(0, right_numbers[right_index],
                                       carried_digit)

        result.appendleft(sum_carried_tuple[0])
        carried_digit = sum_carried_tuple[1]
        right_index -= 1

    if carried_digit != 0:
        result.appendleft(carried_digit)

    return "".join(map(str, result))


def sum_digits(a, b, carried):
    local_sum = a + b + carried
    return local_sum % 2, local_sum // 2


if __name__ == '__main__':
    print(binary_sum(input(), input()))
