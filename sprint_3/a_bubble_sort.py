def bubble_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    for move_index in range(len(arr) - 1):
        for compare_index in range(move_index, len(arr)):
            if arr[move_index] > arr[compare_index]:
                tmp = arr[move_index]
                arr[move_index] = arr[compare_index]
                arr[compare_index] = tmp

    return arr


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        _ = input_txt.readline()
        arr = [int(n) for n in input_txt.readline().split(' ')]
        output_txt.write(
            ' '.join([str(n) for n in bubble_sort(arr)])
        )
