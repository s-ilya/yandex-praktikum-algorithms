__LUCKY_SUM = 1


def digits(n: int) -> list:
    result = []

    while n != 0:
        result.append(n % 10)
        n = n // 10

    return result



if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())
        checked_numbers = set()

        while True:
            sum = 0
            for digit in digits(n):
                sum += digit * digit

            if sum in checked_numbers:
                output_txt.write(str(False))
                break
            elif sum == __LUCKY_SUM:
                output_txt.write(str(True))
                break
            else:
                checked_numbers.add(n)
                n = sum