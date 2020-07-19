from random import randrange
from bisect import bisect_left, bisect_right


def __order_stats(
        first: list,
        first_start: int,
        first_end: int,
        second: list,
        second_start: int,
        second_end: int,
        k: int
):
    first_len = first_end - first_start
    second_len = second_end - second_start
    overall_len = first_len + second_len

    pivot_index = randrange(overall_len)

    pivot = first[first_start + pivot_index] if pivot_index < first_len else second[
        second_start + (pivot_index - first_len)]

    left_first_end = bisect_left(first, pivot, lo=first_start, hi=first_end)
    left_second_end = bisect_left(second, pivot, lo=second_start, hi=second_end)

    right_first_start = bisect_right(first, pivot, lo=first_start, hi=first_end)
    right_second_start = bisect_right(second, pivot, lo=second_start, hi=second_end)

    left_len = (left_first_end - first_start) + (left_second_end - second_start)
    right_len = (first_end - right_first_start) + (second_end - right_second_start)
    pivot_len = overall_len - left_len - right_len

    if k <= left_len:
        return __order_stats(
            first=first,
            first_start=first_start,
            first_end=left_first_end,
            second=second,
            second_start=second_start,
            second_end=left_second_end,
            k=k
        )
    elif left_len < k <= left_len + pivot_len:
        return pivot
    else:
        return __order_stats(
            first=first,
            first_start=right_first_start,
            first_end=first_end,
            second=second,
            second_start=right_second_start,
            second_end=second_end,
            k=k - left_len - pivot_len
        )


def median(first, second):
    if first is None:
        first = []

    if second is None:
        second = []

    overall_len = len(first) + len(second)

    if overall_len == 0:
        raise ValueError()

    # k-th order statistics index starts from 1
    if overall_len % 2 == 1:
        return __order_stats(
            first=first,
            first_start=0,
            first_end=len(first),
            second=second,
            second_start=0,
            second_end=len(second),
            k=(overall_len // 2) + 1
        )
    else:
        median_first_k = (overall_len // 2)
        median_second_k = (overall_len // 2) + 1

        median_first_value = __order_stats(
            first=first,
            first_start=0,
            first_end=len(first),
            second=second,
            second_start=0,
            second_end=len(second),
            k=median_first_k
        )
        median_second_value = __order_stats(
            first=first,
            first_start=0,
            first_end=len(first),
            second=second,
            second_start=0,
            second_end=len(second),
            k=median_second_k
        )

        return (median_first_value + median_second_value) / 2


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
