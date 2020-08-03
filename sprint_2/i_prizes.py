def can_split(items: list, n: int) -> bool:
    overall = sum(items)

    if overall % n != 0:
        return False

    part = overall / n
    parts_collected = 0

    sorted_items = sorted(items, reverse=True)

    current_part = 0
    while len(sorted_items) != 0 and parts_collected < n:
        index_to_take = -1

        for index in range(len(sorted_items)):
            if sorted_items[index] <= part - current_part:
                index_to_take = index
                break

        if index_to_take == -1:
            return False
        else:
            current_part += sorted_items.pop(index_to_take)

        if current_part == part:
            parts_collected += 1
            current_part = 0

    return len(sorted_items) == 0 and parts_collected == n


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())
        _ = int(input_txt.readline())
        items = [int(item) for item in input_txt.readline().split(' ')]

        output_txt.write(str(can_split(items, n)))
