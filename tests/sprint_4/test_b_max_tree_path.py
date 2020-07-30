from unittest import TestCase

from sprint_4.b_max_tree_path import solution, Node


class MaxTreePathTest(TestCase):
    def test_single(self):
        self.assertEqual(1, solution(Node(1)))

    def test_combined_with_left(self):
        self.assertEqual(3, solution(Node(1, left=Node(2))))

    def test_combined_with_right(self):
        self.assertEqual(3, solution(Node(1, right=Node(2))))

    def test_through_root(self):
        self.assertEqual(6, solution(Node(1, left=Node(2), right=Node(3))))

    def test_only_left(self):
        self.assertEqual(10, solution(Node(6, left=Node(4), right=Node(-1))))

    def test_only_right(self):
        self.assertEqual(10, solution(Node(6, right=Node(4), left=Node(-1))))

    def test_only_root(self):
        self.assertEqual(42, solution(Node(42, left=Node(-1), right=Node(-2))))

    def test_subtree(self):
        self.assertEqual(33, solution(Node(-1, left=Node(30, right=Node(3)))))

    def test_sample(self):
        self.assertEqual(
            12,
            solution(
                Node(-5,
                     left=Node(1),
                     right=Node(7,
                                left=Node(2),
                                right=Node(3)))
            )
        )
        self.assertEqual(
            6,
            solution(
                Node(
                    2,
                    left=Node(2),
                    right=Node(-3,
                               left=Node(5),
                               right=Node(1))
                )
            )
        )
        self.assertEqual(
            21,
            solution(
                Node(-1,
                     left=Node(2,
                               left=Node(7,
                                         left=Node(-1)),
                               right=Node(3,
                                          left=Node(9), right=Node(-6))),
                     right=Node(3,
                                left=Node(4), right=Node(0)))
            )
        )
