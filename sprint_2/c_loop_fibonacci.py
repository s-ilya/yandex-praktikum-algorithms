if __name__ == '__main__':
    input_txt = open('input.txt', mode='r')
    output_txt = open('output.txt', mode='w')
    
    n = int(input_txt.readline())

    if n == 0 or n == 1:
        output_txt.write(str(1))
    else:
        previous = 1
        current = 1

        for _ in range(1, n):
            n = previous + current
            previous = current
            current = n

        output_txt.write(str(current))
