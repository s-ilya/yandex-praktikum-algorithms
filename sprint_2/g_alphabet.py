__start = 'a'
__end = 'z'


def az(start=__start, end=__end):
    if start != end:
        return start + ' ' + az(chr(ord(start) + 1), end)
    else:
        return start


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        c = input_txt.readline()
        output_txt.write(az(end=c))
