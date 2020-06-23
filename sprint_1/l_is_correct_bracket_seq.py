__open_bracket_for = dict([(')', '('), ('}', '{'), (']', '[')])


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return len(self.items) == 0


def is_correct_bracket_seq(brackets_sequence: str) -> bool:
    track_brackets = Stack()

    for bracket in brackets_sequence:
        if bracket in __open_bracket_for.keys() and not track_brackets.is_empty() and __open_bracket_for[
            bracket] == track_brackets.peek():
            track_brackets.pop()
        else:
            track_brackets.push(bracket)

    return track_brackets.is_empty()


if __name__ == '__main__':
    print(is_correct_bracket_seq(input()))
