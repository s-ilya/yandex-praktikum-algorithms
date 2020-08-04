def __frequencies(raw_input: str) -> dict:
    result = {}

    if raw_input == '':
        return result

    for item in [int(n) for n in raw_input.split(' ')]:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        input_txt.readline()
        input_txt.readline()

        first_raw = input_txt.readline().strip()
        first = [int(n) for n in first_raw.split(' ')] if first_raw != '' else []
        second = __frequencies(input_txt.readline().strip())

        intersection_in_order = []

        for item in first:
            if item in second:
                if second[item] == 1:
                    del second[item]
                else:
                    second[item] -= 1

                intersection_in_order.append(item)

        output_txt.write(
            ' '.join(
                [str(n) for n in intersection_in_order]
            )
        )
