if __name__ == '__main__':
    n = int(input())
    binary_digits = list()

    while n != 0:
        binary_digits.insert(0, n % 2)
        n = n // 2

    print(
        "".join(
            map(str, binary_digits)
        )
    )
