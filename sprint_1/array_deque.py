from array import array


class ArrayDequeExceedsCapacity(Exception):
    pass


class ArrayDeque:
    def __init__(self, capacity=256):
        self.__capacity = capacity
        self.__size = 0
        self.__items = array('i', [0]) * capacity
        self.__head = 0
        self.__tail = 0

    def push_back(self, item) -> None:
        if self.size() == self.__capacity:
            raise ArrayDequeExceedsCapacity()

        self.__size += 1
        self.__items[self.__tail_index()] = item
        self.__tail += 1

    def push_front(self, item) -> None:
        if self.size() == self.__capacity:
            raise ArrayDequeExceedsCapacity()

        self.__size += 1
        self.__head -= 1

        self.__items[self.__head_index()] = item

    def pop_front(self):
        if self.size() == 0:
            return None

        item = self.__items[self.__head_index()]

        self.__head += 1
        self.__size -= 1

        return item

    def pop_back(self):
        if self.size() == 0:
            return None

        self.__tail -= 1
        self.__size -= 1

        return self.__items[self.__tail_index()]

    def size(self) -> int:
        return self.__size

    def __head_index(self):
        return self.__head % self.__capacity

    def __tail_index(self):
        return self.__tail % self.__capacity

    def __str__(self):
        if self.size() == 0:
            return "[]"

        result = "["

        item_index = self.__head
        while True:
            result += str(self.__items[item_index % self.__capacity])
            item_index += 1

            if item_index != self.__tail:
                result += ", "
            else:
                break

        result += "]"
        return result
