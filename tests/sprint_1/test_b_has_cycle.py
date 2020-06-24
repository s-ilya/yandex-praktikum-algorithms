from unittest import TestCase

from sprint_1.b_has_cycle import hasCycle, Node


class HasCycleTest(TestCase):
    def test_none_no_cycle(self):
        self.assertFalse(hasCycle(None))

    def test_single_node_no_cycle(self):
        self.assertFalse(hasCycle(Node(value=1)))

    def test_single_cycle(self):
        first = Node(value=1)
        first.next = first

        self.assertTrue(hasCycle(first))

    def test_multiple_nodes_cycle(self):
        first = Node(value=1)
        second = Node(value=2, next=first)
        first.next = second

        self.assertTrue(hasCycle(first))
