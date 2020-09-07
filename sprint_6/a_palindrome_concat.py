__reversed_cache = {}

__palindromes_hashes = set()
__non_palindromes_hashes = set()


def __reverse(word):
    if word in __reversed_cache:
        return __reversed_cache[word]

    reversed_word = word[::-1]
    __reversed_cache[word] = reversed_word

    return reversed_word


def __is_palindrome(left, right):
    word = left + right
    word_hash = hash(word)

    if word_hash in __palindromes_hashes:
        return True

    if word_hash in __non_palindromes_hashes:
        return False

    is_palindrome = left + right == __reverse(right) + __reverse(left)

    if is_palindrome:
        __palindromes_hashes.add(word_hash)
    else:
        __non_palindromes_hashes.add(word_hash)

    return is_palindrome


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
                    palindrome_indices.append(str(left_index + 1) + ' ' + str(right_index + 1))

        for palindrome_index in palindrome_indices:
            output_txt.write(palindrome_index + '\n')
