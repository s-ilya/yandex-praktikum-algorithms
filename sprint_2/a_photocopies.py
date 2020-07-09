def get_max_photos_to_backup(capacities: list) -> int:
    non_empty_capacities = list(filter(lambda n: n > 0, capacities))

    if len(non_empty_capacities) <= 1:
        return 0

    sorted_capacities = sorted(non_empty_capacities)
    stored_photos = 0

    while len(sorted_capacities) > 1:
        first = sorted_capacities.pop(0)
        last = sorted_capacities.pop()

        stored_photos += 1

        if first >= 2:
            sorted_capacities.append(first - 1)

        if last >= 2:
            sorted_capacities.append(last - 1)

        sorted_capacities.sort()

    return stored_photos


if __name__ == '__main__':
    input_txt = open('input.txt', mode='r')
    output_txt = open('output.txt', mode='w')

    _ = input_txt.readline()
    capacities = [int(n) for n in input_txt.readline().split(' ')]

    output_txt.write(str(get_max_photos_to_backup(capacities)))
