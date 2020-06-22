from unittest import TestCase, skip
import random

from sprint_1.merge_ids import merge_ids


class MergeIdsTest(TestCase):
    def test_merge_ids(self):
        self.assertEqual([], merge_ids([], []))
        self.assertEqual([1], merge_ids([1], []))

    def test_ends_with_target_idx_eq_source_idx(self):
        self.assertEqual([1, 2], merge_ids([1, 0], [2]))

    def test_has_empty_target(self):
        self.assertEqual([1, 2], merge_ids([0, 0], [1, 2]))

    def test_has_equal_ids(self):
        self.assertEqual([1, 1], merge_ids([1, 0], [1]))

    def test_merges_when_has_only_tmp(self):
        self.assertEqual([1, 2], merge_ids([2, 0], [1]))

    def test_merges_when_has_tmp_and_target__tmp_is_less(self):
        self.assertEqual([1, 2, 3], merge_ids([2, 3, 0], [1]))

    def test_merges_when_has_source_and_tmp__tmp_is_less(self):
        self.assertEqual([1, 2, 3], merge_ids([2, 0, 0], [1, 3]))

    def test_merges_when_has_source_and_tmp__source_is_less(self):
        self.assertEqual([1, 2, 3], merge_ids([3, 0, 0], [1, 2]))

    def test_merges_when_has_all_three__source_is_less(self):
        self.assertEqual([1, 2, 3, 4], merge_ids([3, 4, 0, 0], [1, 2]))

    def test_merges_when_has_all_three__tmp_is_less(self):
        self.assertEqual([1, 2, 3, 4], merge_ids([2, 4, 0, 0], [1, 3]))

    def test_merges_when_has_all_three__tmp_eq_source(self):
        self.assertEqual([1, 2, 3, 3, 5], merge_ids([1, 3, 5, 0, 0], [2, 3]))

    @skip('Randomized testing')
    def test_random(self):
        max_ids = 100

        for _ in range(1000):
            ids_length = random.randrange(1, max_ids)
            target_length = random.randrange(ids_length)
            source_length = ids_length - target_length

            ids = [random.randrange(1, ids_length + 1) for _ in range(ids_length)]
            source = sorted(ids[target_length:])
            target = sorted(ids[:target_length])

            for _ in range(source_length):
                target.append(0)

            print("Target: [" + ", ".join([str(i) for i in target]) + "]")
            print("Source: [" + ", ".join([str(i) for i in source]) + "]")
            self.assertEqual(sorted(ids), merge_ids(target, source))
