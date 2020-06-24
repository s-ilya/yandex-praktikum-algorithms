class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class StackQueue:
    def __init__(self):
        self.__storage = Stack()
        self.__size = 0

    def put(self, value):
        self.__storage.push(value)
        self.__size += 1

    def get(self):
        tmp = Stack()

        while self.__storage.size() > 1:
            tmp.push(self.__storage.pop())

        item = self.__storage.pop()

        while not tmp.is_empty():
            self.__storage.push(tmp.pop())

        self.__size -= 1
        return item

    def get_size(self):
        return self.__size
