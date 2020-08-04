if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        line_n = int(input_txt.readline())
        k = int(input_txt.readline())

        n_line_len = pow(2, line_n - 1)
        digit = 0

        while n_line_len != 1:
            line_middle = n_line_len // 2

            if k > line_middle:
                digit = 0 if digit == 1 else 1
                k -= line_middle

            n_line_len = line_middle

        output_txt.write(str(digit))
