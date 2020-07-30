# https://contest.yandex.ru/contest/18997/run-report/33706576/


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class __MaxPathResult:
    def __init__(self, current_path: int, overall_max: int):
        self.current_path = current_path
        self.overall_max = overall_max


def __append_largest_child_path_or_start_with_current(left: int, right: int, current: int) -> int:
    return current + max(0, left, right)


def __calculate_max_path_weight(current: Node) -> __MaxPathResult:
    if current is None:
        return __MaxPathResult(current_path=0, overall_max=0)

    if current.left is None and current.right is None:
        return __MaxPathResult(current_path=current.value, overall_max=current.value)

    left_max_path = __calculate_max_path_weight(current.left)
    right_max_math = __calculate_max_path_weight(current.right)

    current_path = __append_largest_child_path_or_start_with_current(
        left=left_max_path.current_path,
        right=right_max_math.current_path,
        current=current.value
    )

    with_current_as_root = current.value + left_max_path.current_path + right_max_math.current_path

    return __MaxPathResult(
        current_path=current_path,
        overall_max=max(
            with_current_as_root,
            left_max_path.overall_max,
            right_max_math.overall_max,
            current_path
        )
    )


def solution(root: Node) -> int:
    max_path_result = __calculate_max_path_weight(root)

    return max(
        max_path_result.overall_max,
        max_path_result.current_path
    )
