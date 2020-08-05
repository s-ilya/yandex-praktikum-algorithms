class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def collect_paths(root: Node, path='', collected=None):
    if root is None:
        return

    if collected is None:
        collected = []

    path += str(root.value)

    if root.left is None and root.right is None:
        collected.append(path)
    else:
        collect_paths(root.left, path=path, collected=collected)
        collect_paths(root.right, path=path, collected=collected)


def solution(root: Node) -> int:
    paths = []
    collect_paths(root, collected=paths)

    return sum(map(int, paths))


if __name__ == '__main__':
    root = Node(1,
                left=Node(2),
                right=Node(3,
                           left=Node(4))
                )

    paths = []
    collect_paths(root, collected=paths)

    print(solution(root))
