# https://contest.yandex.ru/contest/18997/run-report/33722008/

from math import floor


class Heap:
    def __init__(self, compare_fn):
        self.__compare_fn = compare_fn
        self.__items = [None]

    @staticmethod
    def __parent_idx(idx):
        return floor(idx / 2)

    @staticmethod
    def __left_child(idx):
        return 2 * idx

    @staticmethod
    def __right_child(idx):
        return (2 * idx) + 1

    def __swap(self, this_idx, that_idx):
        tmp = self.__items[this_idx]
        self.__items[this_idx] = self.__items[that_idx]
        self.__items[that_idx] = tmp

    def push(self, item):
        self.__items.append(item)
        self.__go_top(len(self.__items) - 1)

    def __go_top(self, idx):
        while idx > 1:
            parent_idx = self.__parent_idx(idx)

            if self.__compare_fn(self.__items[parent_idx], self.__items[idx]) > 0:
                self.__swap(idx, parent_idx)
                idx = parent_idx
            else:
                return

    def pop(self):
        if self.size() == 0:
            raise IndexError()

        self.__swap(1, -1)
        result = self.__items.pop()

        self.__go_down(1)

        return result

    def __go_down(self, idx):
        while self.__left_child(idx) < len(self.__items):
            swap_with_idx = idx

            left_child_idx = self.__left_child(idx)
            right_child_idx = self.__right_child(idx)

            if self.__compare_fn(self.__items[left_child_idx], self.__items[swap_with_idx]) < 0:
                swap_with_idx = left_child_idx

            if right_child_idx < len(self.__items) and self.__compare_fn(self.__items[right_child_idx],
                                                                         self.__items[swap_with_idx]) < 0:
                swap_with_idx = right_child_idx

            if swap_with_idx == idx:
                return

            self.__swap(idx, swap_with_idx)
            idx = swap_with_idx

    def size(self):
        return len(self.__items) - 1


def heap_sort(items, compare_fn):
    heap = Heap(compare_fn)

    for item in items:
        heap.push(item)

    result = []

    while heap.size() > 0:
        result.append(heap.pop())

    return result


class Participant:
    def __init__(self, name, points, priority=0):
        self.name = name
        self.points = points
        self.priority = priority

    def positive_points_sum(self):
        result = 0

        for point in self.points:
            result += point if point > 0 else 0

        return result

    @staticmethod
    def from_str(raw_input, priority=0):
        parts = raw_input.split(' ')
        name = parts[0]
        points = [int(n) for n in parts[1:]]

        return Participant(name, points, priority)

    def __str__(self):
        return self.name + ' ' + ' '.join([str(n) for n in self.points])


__KONDRATIY_SET = set('kondratiy')


def compare_participants(this, that):
    this_is_kondratiy = __KONDRATIY_SET.issubset(set(this.name))
    that_is_kondratiy = __KONDRATIY_SET.issubset(set(that.name))

    if that_is_kondratiy and this_is_kondratiy:
        return that.priority - this.priority

    if that_is_kondratiy:
        return 1

    if this_is_kondratiy:
        return -1

    this_points = this.positive_points_sum()
    that_points = that.positive_points_sum()

    if this_points != that_points:
        return that_points - this_points

    if this.name < that.name:
        return -1
    elif this.name == that.name:
        return that.priority - this.priority
    else:
        return 1


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        participants_n = int(input_txt.readline())
        participants = [Participant.from_str(input_txt.readline(), n) for n in range(participants_n)]

        output_txt.writelines([
            str(participant) + '\n' for participant in heap_sort(participants, compare_participants)
        ])
