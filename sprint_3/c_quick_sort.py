def quicksort(nums, start=None, end=None):
    if start is None:
        start = 0

    if end is None:
        end = len(nums) - 1

    if start >= end:
        return

    i, j = start, end
    pivot = end

    while i <= j:
        while nums[i] < pivot:
            i += 1

        while nums[j] > pivot:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    quicksort(nums, start, j)
    quicksort(nums, i, end)


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        _ = input_txt.readline()
        arr = [int(n) for n in input_txt.readline().split(' ')]
        quicksort()

        output_txt.write(
            ' '.join([str(n) for n in arr])
        )
