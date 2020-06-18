def sort_chars_by_frequency(line: str) -> str:
    if len(line) == 0:
        return ""

    frequencies = dict()
    for char in line:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    unique_chars = sorted(frequencies.keys())
    unique_chars = sorted(unique_chars, key=lambda char: frequencies[char], reverse=True)

    chars = list()
    for unique_char in unique_chars:
        for char_index in range(frequencies[unique_char]):
            chars.append(unique_char)

    return "".join(chars)


if __name__ == '__main__':
    print(sort_chars_by_frequency(input()))
