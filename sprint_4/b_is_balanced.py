# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def __collect_stats(root):
    if root.left is None and root.right is None:
        return (1, True)

    left_stats = __collect_stats(root.left) if root.left is not None else (0, True)
    right_stats = __collect_stats(root.right) if root.right is not None else (0, True)

    return (
        1 + max(left_stats[0], right_stats[0]),
        left_stats[1] and right_stats[1] and abs(left_stats[0] - right_stats[0]) <= 1
    )


def solution(root):
    tree_stats = __collect_stats(root)
    return tree_stats[1]


# if __name__ == '__main__':
    # root = Node(1,
    #             left=Node(3,
    #                       left=Node(8,
    #                                 left=Node(14),
    #                                 right=Node(15)),
    #                       right=Node(10,
    #                                  right=Node(3))),
    #             right=Node(5,
    #                        left=Node(-2),
    #                        right=Node(6,
    #                                   left=Node(0),
    #                                   right=Node(1,
    #                                              left=Node(42,
    #                                                        left=Node(43)))))
    #             )

    # root = Node(1,
    #             left=Node(2),
    #             right=Node(0,
    #                        left=Node(3,
    #                                  left=Node(8)),
    #                        right=Node(6)))
    #
    # root = Node(1, left=Node(2, left=Node(3)))
    #
    # print(solution(root))
