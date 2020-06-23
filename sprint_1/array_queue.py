class ArrayQueue:
    def __init__(self, initial_capacity=256):
        self.__capacity = initial_capacity
        self.__size = 0
        self.__items = [None for _ in range(self.__capacity)]
        self.__head = 0
        self.__tail = 0

    def push(self, item) -> None:
        if self.size() == self.__capacity:
            self.__reallocate(self.__capacity * 2)

        self.__size += 1
        self.__items[self.__tail_index()] = item
        self.__tail += 1

    def pop(self):
        if self.size() == 0:
            return None

        item = self.__items[self.__head_index()]

        self.__head += 1
        self.__size -= 1

        if self.size() != 0 and ((self.__capacity // self.size()) >= 4):
            self.__reallocate(self.__capacity // 2)

        return item

    def peek(self):
        return self.__items[self.__head_index()]

    def size(self) -> int:
        return self.__size

    def __head_index(self):
        return self.__head % self.__capacity

    def __tail_index(self):
        return self.__tail % self.__capacity

    def __reallocate(self, capacity):
        new_items = [None for _ in range(capacity)]
        new_item_index = 0
        item_index = self.__head

        while item_index != self.__tail:
            new_items[new_item_index] = self.__items[item_index % self.__capacity]
            item_index += 1
            new_item_index += 1

        self.__head = 0
        self.__tail = self.__size
        self.__capacity = capacity
        self.__items = new_items

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
