if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())
        items = [int(n) for n in input_txt.readline().split(' ')] if n > 0 else []

        zeros = 0
        ones = 0
        twos = 0

        for item in items:
            if item == 0:
                zeros += 1
            elif item == 1:
                ones += 1
            elif item == 2:
                twos += 1

        joined = ['0'] * zeros + ['1'] * ones + ['2'] * twos

        output_txt.write(' '.join(joined))
