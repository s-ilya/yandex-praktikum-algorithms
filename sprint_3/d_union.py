def __parse_or_empty(raw_input: str) -> list:
    if raw_input.strip() == '':
        return []

    return [int(n) for n in raw_input.split(' ')]


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        input_txt.readline()
        input_txt.readline()

        first_list = __parse_or_empty(input_txt.readline())
        second_set = set(__parse_or_empty(input_txt.readline()))

        intersection_in_order = []
        seen_items = set()

        for item in first_list:
            if item in second_set and item not in seen_items:
                intersection_in_order.append(item)

            seen_items.add(item)

        output_txt.write(
            ' '.join(
                [str(n) for n in intersection_in_order]
            )
        )
