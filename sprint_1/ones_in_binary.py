def count_ones(n: int) -> int:
    ones_count = 0

    while n != 0:
        if n % 2 == 1:
            ones_count += 1

        n = n // 2

    return ones_count


if __name__ == '__main__':
    n = int(input())
    print(count_ones(n))