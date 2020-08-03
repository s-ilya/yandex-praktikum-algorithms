# https://contest.yandex.ru/contest/18997/run-report/33703299/

__NOT_CALCULATED = -1

__CACHED_CALCULATION = [__NOT_CALCULATED for _ in range(21)]

__CACHED_CALCULATION[0] = 0
__CACHED_CALCULATION[1] = 1


def count_search_trees(nodes: int) -> int:
    if __CACHED_CALCULATION[nodes] != __NOT_CALCULATED:
        return __CACHED_CALCULATION[nodes]

    possible_trees = 0

    for root_index in range(nodes):
        left_subtree_nodes = root_index
        right_subtree_nodes = nodes - root_index - 1

        left_trees = count_search_trees(left_subtree_nodes)
        right_trees = count_search_trees(right_subtree_nodes)

        possible_trees += max(1, left_trees) * max(1, right_trees)

    __CACHED_CALCULATION[nodes] = possible_trees

    return possible_trees


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        nodes = int(input_txt.readline())
        output_txt.write(str(count_search_trees(nodes)))
