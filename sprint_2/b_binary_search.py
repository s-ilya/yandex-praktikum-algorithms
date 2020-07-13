not_found_index = -1


def binary_search(arr: list, element: int, start: int = 0, stop: int = None) -> int:
    stop = stop if stop is not None else len(arr)

    if stop == start:
        return not_found_index

    if stop - start == 1:
        return start if arr[start] == element else not_found_index

    is_sorted = arr[stop - 1] > arr[start]
    middle_index = (start + stop) // 2

    if is_sorted:
        if element < arr[middle_index]:
            return binary_search(arr, element, start=start, stop=middle_index)
        else:
            return binary_search(arr, element, start=middle_index, stop=stop)
    else:
        index_left = binary_search(arr, element, start=start, stop=middle_index)
        index_right = binary_search(arr, element, start=middle_index, stop=stop)

        return index_left if index_left != not_found_index else index_right


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        _ = input_txt.readline()
        element = int(input_txt.readline())
        arr = [int(n) for n in input_txt.readline().split(' ')]

        output_txt.write(str(binary_search(arr, element)))
