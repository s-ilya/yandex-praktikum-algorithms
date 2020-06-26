# https://contest.yandex.ru/contest/18168/run-report/33546904/

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(head: Node) -> bool:
    limit = pow(2, 20)

    current_node = head
    step = 0

    while step < limit and current_node is not None:
        current_node = current_node.next
        step += 1

    return current_node is not None
