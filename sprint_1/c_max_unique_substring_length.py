from array import array


def max_unique_substring_length(input_string: str) -> int:
    if len(input_string) <= 1:
        return len(input_string)

    max_length = 0
    current_length = 0
    last_seen_indices = array('h', [-1 for _ in range(__max_ascii_code)])

    for letter_index in range(len(input_string)):
        letter = input_string[letter_index]
        code = ord(letter)

        if last_seen_indices[code] == -1:
            last_seen_indices[code] = letter_index
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            this_letter_last_seen_index = last_seen_indices[code]

            for index_index in range(len(last_seen_indices)):
                last_seen_index = last_seen_indices[index_index]

                if last_seen_index != -1 and last_seen_index <= this_letter_last_seen_index:
                    last_seen_indices[index_index] = -1
                    current_length -= 1

            last_seen_indices[code] = letter_index
            current_length += 1

    return max(current_length, max_length)


__max_ascii_code = 123

if __name__ == '__main__':
    print(max_unique_substring_length(input()))
