class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(head: Node) -> bool:
    if head is None:
        return False

    return head.next == head
