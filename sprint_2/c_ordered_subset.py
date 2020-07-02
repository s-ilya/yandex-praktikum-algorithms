def is_ordered_subset(small: str, big: str) -> bool:
    if small == big or small == '':
        return True

    small_stack = list(small)

    for big_item in big:
        if small_stack[0] == big_item:
            small_stack.pop(0)

        if len(small_stack) == 0:
            return True

    return False


if __name__ == '__main__':
    print(is_ordered_subset(input(), input()))
