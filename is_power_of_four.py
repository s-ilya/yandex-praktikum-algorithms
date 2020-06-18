def is_power_of_four(n: int) -> bool:
    if n == 0:
        return False

    while n != 1:
        if n % 4 != 0:
            return False

        n = n // 4

    return True


if __name__ == '__main__':
    n = int(input())
    print(is_power_of_four(n))
