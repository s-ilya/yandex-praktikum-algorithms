if __name__ == '__main__':
    first = input()
    second = input()

    first_set = set(first)
    second_set = set(second)

    print(len(first) == len(second) and first_set == second_set)
