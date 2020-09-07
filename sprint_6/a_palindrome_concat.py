__reversed_cache = {}


def __reverse(word: str) -> str:
    if word in __reversed_cache:
        return __reversed_cache[word]

    reversed_word = word[::-1]
    __reversed_cache[word] = reversed_word

    return reversed_word


def __is_palindrome(left: str, right: str) -> bool:
    return left + right == __reverse(right) + __reverse(left)


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())
        parts = []

        for _ in range(n):
            parts.append(input_txt.readline().strip())

        palindrome_indices = []
        for left_index, left_part in enumerate(parts):
            for right_index, right_part in enumerate(parts):
                if left_index == right_index:
                    continue

                if __is_palindrome(left_part, right_part):
                    palindrome_indices.append((left_index + 1, right_index + 1))

        for palindrome_index in palindrome_indices:
            output_txt.write('{} {}\n'.format(palindrome_index[0], palindrome_index[1]))
