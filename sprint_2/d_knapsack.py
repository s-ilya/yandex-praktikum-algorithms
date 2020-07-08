from operator import itemgetter

__index = 0
__value = 1
__weight = 2


def get_knapsack_contents(capacity: int, items):
    take_indices = list()

    items_by_values = sorted(
        items,
        key=itemgetter(__weight)
    )

    items_by_values = sorted(
        items_by_values,
        key=itemgetter(__value),
        reverse=True
    )

    for item in items_by_values:
        if capacity >= item[__weight]:
            take_indices.append(item[__index])
            capacity -= item[__weight]

            if capacity == 0:
                break

    return sorted(take_indices)


if __name__ == '__main__':
    capacity = int(input())
    n = int(input())
    items = list()

    for item_index in range(n):
        data = [int(chunk) for chunk in input().split(' ')]
        items.append((item_index, data[0], data[1]))

    print(
        ' '.join(
            [str(index) for index in get_knapsack_contents(capacity, items)]
        )
    )
