from datetime import datetime


def binary_sum(left: str, right: str) -> str:
    # checkpoint = datetime.now().microsecond

    left_index = len(left) - 1
    right_index = len(right) - 1
    carried_digit = 0
    result = ""

    # print("After initialization: " + str((datetime.now().microsecond - checkpoint) / 1000))
    # checkpoint = datetime.now().microsecond

    while left_index >= 0 and right_index >= 0:
        local_sum = int(left[left_index]) + int(right[right_index]) + carried_digit

        result = ("1" if local_sum == 1 or local_sum == 3 else "0") + result
        carried_digit = 1 if local_sum > 1 else 0
        left_index -= 1
        right_index -= 1

    # print("After left_index >= 0 and right_index >= 0: " + str((datetime.now().microsecond - checkpoint) / 1000))
    # checkpoint = datetime.now().microsecond

    while left_index >= 0:
        local_sum = int(left[left_index]) + carried_digit

        result = ("1" if local_sum == 1 or local_sum == 3 else "0") + result
        carried_digit = 1 if local_sum > 1 else 0
        left_index -= 1

    # print("After left_index >= 0: " + str((datetime.now().microsecond - checkpoint) / 1000))
    # checkpoint = datetime.now().microsecond

    while right_index >= 0:
        local_sum = int(right[right_index]) + carried_digit

        result = ("1" if local_sum == 1 or local_sum == 3 else "0") + result
        carried_digit = 1 if local_sum > 1 else 0
        right_index -= 1

    # print("After right_index >= 0: " + str((datetime.now().microsecond - checkpoint) / 1000))
    # checkpoint = datetime.now().microsecond

    if carried_digit != 0:
        result = str(carried_digit) + result

    # print("After carried_digit != 0: " + str((datetime.now().microsecond - checkpoint) / 1000))

    return result


def sum_digits(a, b, carried):
    local_sum = a + b + carried
    return local_sum % 2, local_sum // 2


if __name__ == '__main__':
    # first = format(2147483647, 'b')

    # start = datetime.now().microsecond
    # binary_sum_result = binary_sum(first, first)
    # end = datetime.now().microsecond
    #
    # print(binary_sum_result)
    # print((end - start) / 1000)
    print(binary_sum(input(), input()))
