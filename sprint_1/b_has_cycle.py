# https://contest.yandex.ru/contest/18168/run-report/33557631/

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(head: Node) -> bool:
    first = head
    second = head
    should_step_second = False

    while first is not None:
        first = first.next

        if first == second:
            return True

        if should_step_second:
            second = second.next

        should_step_second = not should_step_second

    return False
