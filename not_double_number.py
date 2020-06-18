from typing import List


def not_double_number(numbers: List[int]) -> int:
    frequencies = dict()

    for number in numbers:
        if number in frequencies:
            frequencies[number] += 1
        else:
            frequencies[number] = 1

    for number, frequency in frequencies.items():
        if frequency != 2:
            return number

    return -1


if __name__ == '__main__':
    _ = input()
    numbers = list(map(int, input().split(" ")))
    print(not_double_number(numbers))
