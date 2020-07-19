from random import randrange
from bisect import bisect_left, bisect_right


def __order_stats(first: list, second: list, k: int) -> int:
    overall_len = len(first) + len(second)
    pivot_index = randrange(overall_len)

    pivot = first[pivot_index] if pivot_index < len(first) else second[pivot_index - len(first)]

    left_first = first[:bisect_left(first, pivot)]
    left_second = second[:bisect_left(second, pivot)]

    right_first = first[bisect_right(first, pivot):]
    right_second = second[bisect_right(second, pivot):]

    left_len = len(left_first) + len(left_second)
    right_len = len(right_first) + len(right_second)
    pivot_len = overall_len - left_len - right_len

    if k <= left_len:
        return __order_stats(left_first, left_second, k)
    elif left_len < k <= left_len + pivot_len:
        return pivot
    else:
        return __order_stats(right_first, right_second, k - left_len - pivot_len)


def median(first: list, second: list) -> float:
    if first is None:
        first = []

    if second is None:
        second = []

    overall_len = len(first) + len(second)

    if overall_len == 0:
        raise ValueError()

    # k-th order statistics index starts from 1
    if overall_len % 2 == 1:
        return __order_stats(first, second, (overall_len // 2) + 1)
    else:
        median_first_k = (overall_len // 2)
        median_second_k = (overall_len // 2) + 1
        return (
                       __order_stats(first, second, median_first_k) +
                       __order_stats(first, second, median_second_k)
               ) / 2


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        input_txt.readline()
        input_txt.readline()

        output_txt.write(
            '{:g}'.format(median(
                [int(n) for n in input_txt.readline().split(' ')],
                [int(n) for n in input_txt.readline().split(' ')]
            ))
        )
