def recursive_fibonacci(n: int) -> int:
    if n in [0, 1]:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


if __name__ == '__main__':
    input_txt = open('input.txt', mode='r')
    n = int(input_txt.readline())

    print(recursive_fibonacci(n))