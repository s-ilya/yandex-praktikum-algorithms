class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root1: Node, root2: Node) -> bool:
    values_equal = False

    if root1 is not None and root2 is not None:
        values_equal = root1.value == root2.value
    elif root1 is None and root2 is None:
        values_equal = True

    if not values_equal:
        return False

    left_equal = False

    if root1.left is not None and root2.left is not None:
        left_equal = solution(root1.left, root2.left)
    elif root1.left is None and root2.left is None:
        left_equal = True

    right_equal = False

    if root1.right is not None and root2.right is not None:
        right_equal = solution(root1.right, root2.right)
    elif root1.right is None and root2.right is None:
        right_equal = True

    return left_equal and right_equal


# if __name__ == '__main__':
