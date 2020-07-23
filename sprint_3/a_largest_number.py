# https://contest.yandex.ru/contest/18883/run-report/33656926/
from typing import List
from functools import cmp_to_key


def __compare_parts(a: str, b: str) -> int:
    ab = "{}{}".format(a, b)
    ba = "{}{}".format(b, a)

    return int(ab) - int(ba)


def largest_number(parts: List[int]) -> int:
    if len(parts) == 0:
        return 0

    parts_value_decreasing = sorted(
        [str(n) for n in parts],
        key=cmp_to_key(__compare_parts),
        reverse=True
    )

    return int("".join(parts_value_decreasing))


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        _ = input_txt.readline()
        parts = [int(s) for s in input_txt.readline().split(' ')]
        output_txt.write(str(largest_number(parts)))
