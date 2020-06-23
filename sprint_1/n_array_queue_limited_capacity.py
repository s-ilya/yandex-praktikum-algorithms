class ArrayQueueExceedingCapacity(Exception):
    pass


class ArrayQueue:
    def __init__(self, initial_capacity=256):
        self.__capacity = initial_capacity
        self.__size = 0
        self.__items = [None for _ in range(self.__capacity)]
        self.__head = 0
        self.__tail = 0

    def push(self, item) -> None:
        if self.size() == self.__capacity:
            raise ArrayQueueExceedingCapacity()

        self.__size += 1
        self.__items[self.__tail_index()] = item
        self.__tail += 1

    def pop(self):
        if self.size() == 0:
            return None

        item = self.__items[self.__head_index()]

        self.__head += 1
        self.__size -= 1

        return item

    def peek(self):
        return self.__items[self.__head_index()]

    def size(self) -> int:
        return self.__size

    def __head_index(self):
        return self.__head % self.__capacity

    def __tail_index(self):
        return self.__tail % self.__capacity


if __name__ == '__main__':
    commands_n = int(input())
    queue_capacity = int(input())

    queue = ArrayQueue(queue_capacity)

    for _ in range(commands_n):
        command = input()

        if command == 'peek':
            print(queue.peek())
        elif command.startswith('push'):
            n = int(command.split(" ")[1])

            try:
                queue.push(n)
            except ArrayQueueExceedingCapacity:
                print('error')
        elif command.startswith('size'):
            print(queue.size())
        elif command == 'pop':
            print(queue.pop())
