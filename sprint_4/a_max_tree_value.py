class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def __max_tree_value(root, current_max=None):
    current_max = max(current_max, root.value) if current_max is not None else root.value

    left_max = __max_tree_value(root.left, current_max) if root.left is not None else current_max
    right_max = __max_tree_value(root.right, current_max) if root.right is not None else current_max

    return max(current_max, left_max, right_max)


def solution(root):
    return __max_tree_value(root)


if __name__ == '__main__':
    root = Node(1,
                left=Node(3,
                          left=Node(8,
                                    left=Node(14),
                                    right=Node(15)),
                          right=Node(10,
                                     right=Node(3))),
                right=Node(5,
                           left=Node(-2),
                           right=Node(6,
                                      left=Node(0),
                                      right=Node(1)))
                )

    print(solution(root))
