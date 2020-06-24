from unittest import TestCase

from sprint_1.c_stack_queue import StackQueue


class StackQueueTest(TestCase):
    def setUp(self) -> None:
        self.q = StackQueue()

    def test_get_size_after_create(self):
        self.assertEqual(0, self.q.get_size())

    def test_get_size_after_put(self):
        self.q.put(1)
        self.assertEqual(1, self.q.get_size())

    def test_get_size_after_put_and_get(self):
        self.q.put(1)
        self.q.put(2)
        self.q.get()
        self.assertEqual(1, self.q.get_size())

    def test_get_single(self):
        self.q.put(1)
        self.assertEqual(1, self.q.get())

    def test_get_multiple(self):
        self.q.put(1)
        self.q.put(2)
        self.assertEqual(1, self.q.get())
        self.assertEqual(2, self.q.get())

    def test_get_put_mixed(self):
        self.q.put(1)
        self.q.put(2)
        self.assertEqual(1, self.q.get())
        self.q.put(3)
        self.q.put(4)
        self.assertEqual(2, self.q.get())
        self.assertEqual(3, self.q.get())
        self.assertEqual(4, self.q.get())
