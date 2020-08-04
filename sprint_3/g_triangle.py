if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())
        lengths = sorted(
            [int(n) for n in input_txt.readline().split(' ')] if n >= 3 else [],
            reverse=True
        )

        max_triangle = 0

        for index in range(n - 2):
            if lengths[index] < lengths[index + 1] + lengths[index + 2]:
                max_triangle = lengths[index] + lengths[index + 1] + lengths[index + 2]
                break

        output_txt.write(str(max_triangle))
