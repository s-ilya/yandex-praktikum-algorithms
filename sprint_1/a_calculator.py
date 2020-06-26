# https://contest.yandex.ru/contest/18168/run-report/33545328/

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


__operations = ["*", "/", "+", "-"]


def calculator(expression: str) -> int:
    if len(expression) == 0:
        return 0

    operands = Stack()

    for input_char in expression.split(" "):
        if input_char in __operations:
            right_operand = operands.pop()
            left_operand = operands.pop()

            if input_char == "/":
                operands.push(left_operand // right_operand)
            elif input_char == "*":
                operands.push(left_operand * right_operand)
            elif input_char == "+":
                operands.push(left_operand + right_operand)
            elif input_char == "-":
                operands.push(left_operand - right_operand)
        else:
            operands.push(int(input_char))

    return operands.pop()


if __name__ == '__main__':
    expression = input()
    print(calculator(expression))
