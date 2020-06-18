import re

if __name__ == '__main__':
    line = input().lower()
    non_letter_re = re.compile("[^a-z|0-9]+")
    clear_line = re.sub(non_letter_re, "", line)

    is_palindrome = True
    left_index = 0
    right_index = len(clear_line) - 1

    if len(clear_line) == 0:
        is_palindrome = False

    while is_palindrome and left_index < right_index:
        if clear_line[left_index] != clear_line[right_index]:
            is_palindrome = False
        else:
            left_index += 1
            right_index -= 1

    print(is_palindrome)
