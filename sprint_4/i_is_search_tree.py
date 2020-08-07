class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> bool:
    left = root.value > root.left.value and solution(root.left) if root.left is not None else True
    right = root.value < root.right.value and solution(root.right) if root.right is not None else True

    return left and right


if __name__ == '__main__':
    root = Node(42,
                left=Node(31, left=Node()),
                right=Node(43, right=Node(44)))

    print(
        solution(root)
    )
