memo = {
    0: 1,
    1: 1
}


def memoized_recursive_fibonacci(n: int) -> int:
    if n in memo.keys():
        return memo[n]

    memo[n] = memoized_recursive_fibonacci(n - 1) + memoized_recursive_fibonacci(n - 2)
    return memo[n]


if __name__ == '__main__':
    input_txt = open('input.txt', mode='r')
    n = int(input_txt.readline())

    print(memoized_recursive_fibonacci(n))
