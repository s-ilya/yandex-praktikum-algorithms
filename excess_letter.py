def excess_letter(s: str, t: str) -> str:
    s_sorted = sorted(s)
    t_sorted = sorted(t)

    s_index = 0
    t_index = 0
    result = ""

    while s_index < len(s_sorted) and t_index < len(t_sorted):
        if s_sorted[s_index] != t_sorted[t_index]:
            result = t_sorted[t_index]
            break

        s_index += 1
        t_index += 1

    if result == "":
        result = t_sorted[-1]

    return result


if __name__ == '__main__':
    print(excess_letter(input(), input()))
