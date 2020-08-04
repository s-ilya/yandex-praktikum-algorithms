def __frequencies(items):
    result = {}

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n_sort = int(input_txt.readline())
        raw_items = input_txt.readline()
        items = __frequencies(
            [int(n) for n in raw_items.split(' ')] if n_sort != 0 else []
        )

        n_order = int(input_txt.readline())
        raw_order = input_txt.readline()
        order = [int(n) for n in raw_order.split(' ')] if n_order != 0 else []

        result = []
        for order_item in order:
            if order_item in items:
                result += [order_item] * items[order_item]
                del items[order_item]

        natural_order_part = []
        for natural_order_item in items.keys():
            natural_order_part += [natural_order_item] * items[natural_order_item]

        output_txt.write(
            ' '.join([str(n) for n in result + sorted(natural_order_part)])
        )
