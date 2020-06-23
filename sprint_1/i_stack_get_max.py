class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def max(self):
        if len(self.items) == 0:
            return None

        max_item = self.items[0]
        for item in self.items[1:]:
            max_item = max(max_item, item)

        return max_item


if __name__ == '__main__':
    commands_n = int(input())
    stack = Stack()

    for _ in range(commands_n):
        command = input()

        if command == 'get_max':
            print(stack.max())
        elif command.startswith('push'):
            n = int(command.split(" ")[1])
            stack.push(n)
        elif command == 'pop':
            try:
                stack.pop()
            except IndexError:
                print("error")
