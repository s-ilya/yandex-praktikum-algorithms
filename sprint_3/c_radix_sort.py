from typing import List

__max_digits = 6


def __counting_sort(arr: List[int], digit_place: int) -> List[int]:
    partitions_by_digit: List[List[int]] = [list() for _ in range(10)]

    for n in arr:
        partitions_by_digit[(n // pow(10, digit_place)) % 10].append(n)

    result = list()

    for rank in partitions_by_digit:
        result += rank

    return result


def radix_sort(arr: List[int]) -> List[int]:
    digit_place = 0
    result = arr

    while digit_place <= __max_digits:
        result = __counting_sort(result, digit_place=digit_place)
        digit_place += 1

    return result


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        input_txt.readline()
        sorted = radix_sort(
            [int(n) for n in input_txt.readline().split(' ')]
        )

        output_txt.write(
            ' '.join(
                [str(n) for n in sorted]
            )
        )
