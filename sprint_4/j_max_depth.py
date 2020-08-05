class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> int:
    if root is None:
        return 0

    left_depth = solution(root.left)
    right_depth = solution(root.right)

    return 1 + max(left_depth, right_depth)


if __name__ == '__main__':
    root = Node(1,
                left=Node(2),
                right=Node(3,
                           right=Node(4)))

    print(
        solution(root)
    )