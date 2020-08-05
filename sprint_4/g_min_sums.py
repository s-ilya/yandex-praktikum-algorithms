from functools import cmp_to_key
from operator import itemgetter, attrgetter
from heapq import heappush, heappop


###
def __cmp_pairs(left, right):
    left_sum = left[0] + left[1]
    right_sum = right[0] + right[1]

    if left_sum != right_sum:
        return left_sum - right_sum
    else:
        return left[0] - right[0]


def __reorder_tuple(tuple):
    one = tuple[0]
    two = tuple[1]

    return min(one, two), max(one, two)


def __tuple_to_pair(tuple):
    return Pair(tuple[0], tuple[1])


def min_sums_arrays(left: list, right: list, k: int) -> list:
    pairs = []

    for left_item in left:
        for right_item in right:
            pairs.append((left_item, right_item))

    sorted_pairs = sorted(pairs, key=cmp_to_key(__cmp_pairs))[:k]
    reordered = map(__reorder_tuple, sorted_pairs)

    return list(map(__tuple_to_pair, sorted(reordered, key=itemgetter(0))))


###

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def __eq__(self, other):
        return self.sum() == other.sum()

    def __lt__(self, other):
        return self.sum() < other.sum() or (self.sum() == other.sum() and self.first < other.first)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return self.sum() > other.sum() or (self.sum() == other.sum() and self.first > other.first)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __str__(self) -> str:
        return '{} {}'.format(self.first, self.second)


def __reorder_pair(pair):
    one = pair.first
    two = pair.second

    return Pair(first=min(one, two), second=max(one, two))


def min_sums(left: list, right: list, k: int) -> list:
    pairs = []
    for left_item in left:
        for right_item in right:
            heappush(pairs, Pair(left_item, right_item))

    k_min = []
    for _ in range(k):
        k_min.append(heappop(pairs))

    return list(sorted(map(__reorder_pair, k_min), key=attrgetter('first')))


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        input_txt.readline()
        left = [int(n) for n in input_txt.readline().strip().split(' ')]

        input_txt.readline()
        right = [int(n) for n in input_txt.readline().strip().split(' ')]

        k = int(input_txt.readline())

        for pair in min_sums_arrays(left, right, k):
            output_txt.write('{} {}\n'.format(pair.first, pair.second))
