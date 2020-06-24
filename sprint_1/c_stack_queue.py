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
    def __init__(self, bucket_capacity=100):
        self.__buckets = Stack()
        self.__size = 0
        self.__bucket_capacity = bucket_capacity

    def put(self, value):
        if self.__buckets.is_empty():
            self.__buckets.push(Stack())

        has_space_in_top_bucket = self.__buckets.peek().size() < self.__bucket_capacity
        top_bucket = self.__buckets.pop() if has_space_in_top_bucket else Stack()

        top_bucket.push(value)

        self.__buckets.push(top_bucket)
        self.__size += 1

    def get(self):
        tmp_buckets = Stack()
        while self.__buckets.size() > 1:
            tmp_buckets.push(self.__buckets.pop())

        bottom_bucket = self.__buckets.pop()

        tmp_items = Stack()
        while bottom_bucket.size() > 1:
            tmp_items.push(bottom_bucket.pop())

        item = bottom_bucket.pop()

        while not tmp_items.is_empty():
            bottom_bucket.push(tmp_items.pop())

        if not bottom_bucket.is_empty():
            self.__buckets.push(bottom_bucket)

        while not tmp_buckets.is_empty():
            self.__buckets.push(tmp_buckets.pop())

        self.__size -= 1
        return item

    def get_size(self):
        return self.__size


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
