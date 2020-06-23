class Stack:
    def __init__(self):
        self.items = []
        self.seen_items = set()

    def push(self, item):
        if item not in self.seen_items:
            self.items.append(item)
            self.seen_items.add(item)

    def pop(self):
        item = self.items.pop()
        self.seen_items.discard(item)
        return item

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


if __name__ == '__main__':
    commands_n = int(input())
    stack = Stack()

    for _ in range(commands_n):
        command = input()

        if command.startswith('push'):
            n = int(command.split(" ")[1])
            stack.push(n)
        elif command == 'pop':
            if stack.size() == 0:
                print("error")
            else:
                stack.pop()
        elif command == 'size':
            print(stack.size())
        elif command == 'peek':
            if stack.size() == 0:
                print("error")
            else:
                print(stack.peek())
