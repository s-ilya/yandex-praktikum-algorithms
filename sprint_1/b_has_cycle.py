# https://contest.yandex.ru/contest/18168/run-report/33565246/


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def __advance(node: Node, steps=1) -> Node:
    step = 0

    while step < steps and node is not None:
        node = node.next
        step += 1

    return node


def hasCycle(head: Node) -> bool:
    first = head
    second = head

    while True:
        first = __advance(first, steps=2)
        second = __advance(second, steps=1)

        if first is None:
            return False
        elif first == second:
            return True
