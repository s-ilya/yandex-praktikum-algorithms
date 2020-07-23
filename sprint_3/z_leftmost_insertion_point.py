def leftmost_insort_index(arr: list, element: int, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(arr)

    while (high - low) > 1:
        arr_len = high - low
        middle_index = low + (arr_len // 2)

        if element < arr[middle_index]:
            high = middle_index
        else:
            low = middle_index

    arr_len = high - low

    if arr_len == 0:
        return low

    if arr_len == 1:
        return low if arr[low] >= element else low + 1
