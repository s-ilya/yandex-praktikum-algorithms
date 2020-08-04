if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())

        items = [int(n) for n in input_txt.readline().split(' ')] if n != 0 else []

        even = list(filter(lambda a: a % 2 == 0, items))
        odd = list(filter(lambda a: a % 2 != 0, items))

        sorted = []

        even_position = True

        while len(even) != 0 and len(odd) != 0:
            sorted.append(
                (even if even_position else odd).pop(0)
            )

            even_position = not even_position

        while len(even) != 0:
            sorted.append(even.pop(0))

        while len(odd) != 0:
            sorted.append(odd.pop(0))

        output_txt.write(
            ' '.join(
                [str(n) for n in sorted]
            )
        )
