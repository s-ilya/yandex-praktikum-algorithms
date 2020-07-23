from typing import List


def __leftmost_insort_index(arr: List[int], element: int, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(arr)

    while (high - low) > 1:
        arr_len = high - low
        middle_index = low + (arr_len // 2)

        if element < arr[middle_index]:
            high = middle_index
        else:
            low = middle_index

    arr_len = high - low

    if arr_len == 0:
        return low

    if arr_len == 1:
        return low if arr[low] >= element else low + 1


def __rightmost_insort_index(arr: List[int], element: int, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(arr)

    while (high - low) > 1:
        arr_len = high - low
        middle_index = low + (arr_len // 2)

        if element < arr[middle_index]:
            high = middle_index
        else:
            low = middle_index

    arr_len = high - low

    if arr_len == 0:
        return low

    if arr_len == 1:
        return low if arr[low] > element else low + 1


def __order_stats(
        first: List[int],
        first_start: int,
        first_end: int,
        second: List[int],
        second_start: int,
        second_end: int,
        k: int
):
    first_len = first_end - first_start
    second_len = second_end - second_start
    overall_len = first_len + second_len

    if first_len >= second_len:
        pivot_index = first_len // 2
        pivot = first[first_start + pivot_index]
    else:
        pivot_index = second_len // 2
        pivot = second[second_start + pivot_index]

    left_first_end = __leftmost_insort_index(first, pivot, low=first_start, high=first_end)
    left_second_end = __leftmost_insort_index(second, pivot, low=second_start, high=second_end)

    right_first_start = __rightmost_insort_index(first, pivot, low=first_start, high=first_end)
    right_second_start = __rightmost_insort_index(second, pivot, low=second_start, high=second_end)

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


def median(first: List[int], second: List[int]) -> int:
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
