from typing import List


def three_days_stats(stats: List[int]) -> int:
    max_multiplication = -1

    for first_index in range(0, len(stats)):
        for second_index in range(first_index, len(stats)):
            for third_index in range(second_index, len(stats)):
                first_value = stats[first_index]
                second_value = stats[second_index]
                third_value = stats[third_index]

                if (first_value + second_value + third_value) == 0:
                    new_max = first_value * second_value * third_value
                    if new_max > max_multiplication and new_max > 0:
                        max_multiplication = new_max

    return max_multiplication


if __name__ == '__main__':
    _ = input()
    print(str(three_days_stats(list(map(int, input().split(" "))))))
