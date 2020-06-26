# https://contest.yandex.ru/contest/18168/run-report/33553597/


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
        self.__stack = Stack()
        self.__is_in_stack_order = True

    def put(self, value):
        if not self.__is_in_stack_order:
            self.__reverse_stack()

        self.__stack.push(value)

    def get(self):
        if self.__is_in_stack_order:
            self.__reverse_stack()

        return self.__stack.pop()

    def get_size(self):
        return self.__stack.size()

    def __reverse_stack(self):
        reversed_stack = Stack()

        while not self.__stack.is_empty():
            reversed_stack.push(self.__stack.pop())

        self.__is_in_stack_order = not self.__is_in_stack_order
        self.__stack = reversed_stack


if __name__ == '__main__':
    commands_n = int(input())

    queue = StackQueue()

    for _ in range(commands_n):
        command = input()

        if command.startswith("put"):
            n = int(command.split(" ")[1])
            queue.put(n)
        elif command == "get":
            if queue.get_size() == 0:
                print("error")
            else:
                print(str(queue.get()))
        elif command == "get_size":
            print(queue.get_size())
