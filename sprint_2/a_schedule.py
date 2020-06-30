# from dataclasses import dataclass
# from typing import List
from operator import itemgetter


#
# @dataclass()
# class Segment:
#     start: float
#     end: float
#
#     def __str__(self) -> str:
#         return '{:g} {:g}'.format(self.start, self.end)


def max_disjoint_segments(segments):
    result = list()

    sorted_by_start_end = sorted(
        segments, key=itemgetter(1, 0),
    )
    current_end = 0

    for segment in sorted_by_start_end:
        if segment[0] >= current_end:
            current_end = segment[1]
            result.append(segment)

    return result


if __name__ == '__main__':
    n = int(input())

    segments = list()
    for _ in range(n):
        start_end = [float(point) for point in input().split(' ')]
        segments.append(start_end)

    disjoint_segments = max_disjoint_segments(segments)
    print(len(disjoint_segments))
    for segment in disjoint_segments:
        print('{:g} {:g}'.format(segment[0], segment[1]))
