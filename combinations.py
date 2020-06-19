from typing import List, Deque
from collections import deque

codes = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def combinations(input: str) -> List[str]:
    if len(input) == 0:
        return []

    input_deque = deque(input)
    result_combinations = list(codes[input_deque.popleft()])

    return __append(result_combinations, input_deque)


def __append(existing_combinations: List[str], input: Deque[str]) -> List[str]:
    if len(input) == 0:
        return existing_combinations

    result = list()
    current_codes = codes[input.popleft()]

    for existing_combination in existing_combinations:
        for current_code in current_codes:
            result.append(existing_combination + current_code)

    return __append(result, input)


if __name__ == '__main__':
    print(
        " ".join(combinations(input()))
    )
