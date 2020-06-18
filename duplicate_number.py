if __name__ == '__main__':
    _ = input()
    numbers = list(map(int, input().split(" ")))
    seen_numbers = set()

    for number in numbers:
        if number not in seen_numbers:
            seen_numbers.add(number)
        else:
            print(number)
            break
