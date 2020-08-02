from unittest import TestCase
from random import randrange
from functools import cmp_to_key

from sprint_4.c_heap_sort import heap_sort


def int_cmp(a, b):
    return a - b


class TestHeapSort(TestCase):
    def test_empty(self):
        self.assertEqual([], heap_sort([], int_cmp))

    def test_single(self):
        self.assertEqual([1], heap_sort([1], int_cmp))

    def test_two_in_order(self):
        self.assertEqual([1, 2], heap_sort([1, 2], int_cmp))

    def test_two_reverse(self):
        self.assertEqual([1, 2], heap_sort([2, 1], int_cmp))

    # 6, 9, 4, 7, 1, 4, 5
    # 0, 5, 2, 7, 0, 3, 0

    def test_sample(self):
        # self.assertEqual(
        #     sorted([0, 5, 2, 7, 0, 3, 0]),
        #     heap_sort([0, 5, 2, 7, 0, 3, 0], int_cmp)
        # )
        # self.assertEqual(
        #     sorted([6, 9, 4, 7, 1, 4, 5]),
        #     heap_sort([6, 9, 4, 7, 1, 4, 5], int_cmp)
        # )
        self.assertEqual(
            sorted([2, 4, 4, 5, 9, 1]),
            heap_sort([2, 4, 4, 5, 9, 1], int_cmp)
        )

    def test_random(self):
        max = 100

        for _ in range(100000):
            n = randrange(0, 100)
            items = [randrange(max) for _ in range(n)]

            # print(
            #     'Case: [{}]'.format(', '.join([str(n) for n in items]))
            # )

            self.assertEqual(
                sorted(items.copy(), key=cmp_to_key(int_cmp)),
                heap_sort(items.copy(), int_cmp),
                msg='Failed for {}'.format(', '.join([str(n) for n in items]))

            )
            # print('Done for {}'.format(str(len(items))))
