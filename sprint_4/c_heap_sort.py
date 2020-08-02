from math import floor


class MaxHeap:
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

            if self.__compare_fn(self.__items[idx], self.__items[left_child_idx]) > 0:
                swap_with_idx = left_child_idx

            if right_child_idx < len(self.__items) \
                    and self.__compare_fn(self.__items[idx], self.__items[right_child_idx]) > 0 \
                    and self.__compare_fn(self.__items[left_child_idx], self.__items[right_child_idx]) > 0:
                swap_with_idx = right_child_idx

            if swap_with_idx == idx:
                return

            self.__swap(idx, swap_with_idx)
            idx = swap_with_idx

    def size(self):
        return len(self.__items) - 1


def heap_sort(items: list, compare_fn) -> list:
    heap = MaxHeap(compare_fn)

    for item in items:
        heap.push(item)

    result = []

    while heap.size() > 0:
        result.append(heap.pop())

    return result
