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


if __name__ == '__main__':
    n = int(input())
    linked_list = LinkedList()

    for _ in range(n):
        linked_list.append(input())

    remove_index = int(input())

    reversed_linked_list = linked_list.reversed()
    reversed_linked_list.pop(remove_index)

    while not reversed_linked_list.is_empty():
        print(reversed_linked_list.pop())
