from typing import List

__empty_value = 0


def __copy(source: List[int], target: List[int], target_start_idx: int) -> None:
    source_copy_idx = 0
    target_copy_idx = target_start_idx

    while source_copy_idx < len(source):
        target[target_copy_idx] = source[source_copy_idx]
        target_copy_idx += 1
        source_copy_idx += 1


def merge_ids(target: List[int], source: List[int]) -> List[int]:
    if len(source) == 0:
        return target

    target_empty_idx = len(target) - len(source)
    __copy(source, target, target_empty_idx)

    target_idx = 0
    source_idx = target_empty_idx
    tmp_read_idx = 0
    tmp_write_idx = 0
    tmp = source

    while target_idx < len(target) and target_idx != source_idx:
        has_tmp = tmp_read_idx != tmp_write_idx
        has_source = source_idx < len(target)
        has_target = target[target_idx] != __empty_value

        if has_target and has_source and has_tmp:
            target_value = target[target_idx]
            source_value = target[source_idx]
            tmp_value = tmp[tmp_read_idx % len(tmp)]

            if source_value < target_value and source_value <= tmp_value:
                tmp[tmp_write_idx % len(tmp)] = target_value
                tmp_write_idx += 1

                target[target_idx] = source_value

                target[source_idx] = __empty_value
                source_idx += 1

            if tmp_value < target_value and tmp_value < source_value:
                tmp[tmp_write_idx % len(tmp)] = target_value
                tmp_write_idx += 1

                target[target_idx] = tmp_value

                tmp_read_idx += 1

        elif has_target and has_source:
            target_value = target[target_idx]
            source_value = target[source_idx]

            if source_value < target_value:
                tmp[tmp_write_idx % len(tmp)] = target_value
                tmp_write_idx += 1

                target[target_idx] = source_value
                target[source_idx] = __empty_value
                source_idx += 1

        elif has_target and has_tmp:
            target_value = target[target_idx]
            tmp_value = tmp[tmp_read_idx % len(tmp)]

            if tmp_value < target_value:
                tmp[tmp_write_idx % len(tmp)] = target_value
                tmp_write_idx += 1

                target[target_idx] = tmp_value
                tmp_read_idx += 1

        elif has_tmp and has_source:
            tmp_value = tmp[tmp_read_idx % len(tmp)]
            source_value = target[source_idx]

            if tmp_value < source_value:
                target[target_idx] = tmp_value
                tmp_read_idx += 1
            else:
                target[target_idx] = source_value
                target[source_idx] = __empty_value
                source_idx += 1

        elif has_tmp:
            target[target_idx] = tmp[tmp_read_idx % len(tmp)]
            tmp_read_idx += 1

        target_idx += 1

    return target


if __name__ == '__main__':
    target = [int(i) for i in input().split(" ")]
    _ = input()
    _ = input()
    source = [int(i) for i in input().split(" ")]

    print(" ".join(str(i) for i in merge_ids(target, source)))
