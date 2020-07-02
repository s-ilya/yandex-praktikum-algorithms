from typing import List


def max_income(stonks: List[int]) -> int:
    account = 0

    while len(stonks) >= 2:
        account -= stonks.pop(0)
        account += stonks.pop(0)

    return account

