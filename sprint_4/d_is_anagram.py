class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def __collect_levels(root, level=0, levels=None):
    if levels is None:
        levels = []

    while level >= len(levels):
        levels.append([])

    if root is not None:
        levels[level].append(root.value)

        __collect_levels(root.left, level + 1, levels)
        __collect_levels(root.right, level + 1, levels)
    else:
        levels[level].append(None)

    return levels


def solution(root: Node) -> bool:
    levels = __collect_levels(root)

    for index, level in enumerate(levels):
        if index == 0:
            continue

        if len(level) % 2 == 0 and level[:len(level) // 2] == list(reversed(level[len(level) // 2:])):
            pass
        else:
            return False

    return True


# if __name__ == '__main__':
#     # root = Node(1,
#     #             left=Node(3,
#     #                       left=Node(8,
#     #                                 left=Node(14),
#     #                                 right=Node(15)),
#     #                       right=Node(10,
#     #                                  right=Node(3))),
#     #             right=Node(5,
#     #                        left=Node(-2),
#     #                        right=Node(6,
#     #                                   left=Node(0),
#     #                                   right=Node(1,
#     #                                              left=Node(42,
#     #                                                        left=Node(43)))))
#     #             )
#
#     # root = Node(1,
#     #             left=Node(2),
#     #             right=Node(0,
#     #                        left=Node(3,
#     #                                  left=Node(8)),
#     #                        right=Node(6)))
#     #
#     root = Node(1,
#                 left=Node(2,
#                           left=Node(3)),
#                 right=Node(2,
#                            left=Node(3)))
#
#     print(solution(root))
