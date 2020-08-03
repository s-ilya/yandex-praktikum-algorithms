if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())

        factorial = 1

        while n > 1:
            factorial *= n
            n -= 1

        output_txt.write(str(factorial))
