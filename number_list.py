def to_number(digits_list):
    number = 0

    for power_of_ten, digit in enumerate(reversed(digits_list)):
        number += digit * pow(10, power_of_ten)

    return number


def to_digits_list(number):
    digits = list()

    while number != 0:
        remainder = number % 10

        digits.insert(0, remainder)
        number = number // 10

    return digits


if __name__ == '__main__':
    x_length = int(input())
    x_list = list(map(int, input().split(" ")))
    k = int(input())

    result = to_digits_list(to_number(x_list) + k)

    print(" ".join(list(map(str, result))))
