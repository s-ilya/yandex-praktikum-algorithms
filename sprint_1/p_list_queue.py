class Node:
    def __init__(self, value=None):
        self.prev = None
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.tail = Node()
        self.head = self.tail

    def is_empty(self):
        return self.head == self.tail

    def first(self):
        return self.head

    def append(self, value):
        node = Node(value)

        if self.is_empty():
            self.head = node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            last_node = self.tail.prev
            last_node.next = node

            node.prev = last_node
            node.next = self.tail

            self.tail.prev = node

    def reversed(self):
        reversed = LinkedList()

        if self.is_empty():
            return reversed

        current_node = self.tail.prev
        while current_node is not None:
            reversed.append(current_node.value)
            current_node = current_node.prev

        return reversed

    def insert(self, value, before=0):
        node = Node(value)

        if before <= 0 or self.is_empty():
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            before_node = self.__find_by_index(before)

            before_node.prev.next = node
            node.prev = before_node.prev

            before_node.prev = node
            node.next = before_node

    def pop(self, index=0):
        if index == 0:
            first = self.head
            self.head = first.next

            return first.value
        else:
            pop_node = self.__find_by_index(index)

            pop_node.prev.next = pop_node.next
            pop_node.next.prev = pop_node.prev

            return pop_node.value

    def __find_by_index(self, index):
        current_node = self.head
        current_index = 0

        while current_index != index and current_node != self.tail:
            current_node = current_node.next
            current_index += 1

        return current_node

    def find_index(self, value):
        current_node = self.head
        current_index = 0

        while current_node != self.tail:
            if current_node.value == value:
                return current_index
            else:
                current_node = current_node.next
                current_index += 1

        return -1

    def __str__(self):
        result = "["

        current_node = self.head

        while current_node != self.tail:
            result += str(current_node.value)

            if current_node.next != self.tail:
                result += ", "

            current_node = current_node.next

        result += "]"

        return result


class ListQueueEmptyError(Exception):
    pass


class ListQueue:
    def __init__(self):
        self.__items = LinkedList()
        self.__size = 0

    def put(self, value):
        self.__items.append(value)
        self.__size += 1

    def get(self):
        if self.size() == 0:
            raise ListQueueEmptyError()

        self.__size -= 1
        return self.__items.pop()

    def size(self):
        return self.__size

    def __str__(self):
        return str(self.__items)


if __name__ == '__main__':
    commands_n = int(input())
    queue = ListQueue()

    for _ in range(commands_n):
        command = input()

        if command == 'get':
            try:
                print(queue.get())
            except ListQueueEmptyError:
                print('error')
        elif command.startswith('put'):
            n = int(command.split(" ")[1])
            queue.put(n)
        elif command == 'size':
            print(queue.size())
