from unittest import TestCase

from sprint_1.array_queue import ArrayQueue


class ArrayQueueTest(TestCase):
    def setUp(self) -> None:
        self.queue = ArrayQueue()

    def test_size_new(self):
        self.assertEqual(0, self.queue.size())

    def test_size_push(self):
        self.queue.push("a")
        self.assertEqual(1, self.queue.size())

    def test_size_pop(self):
        self.queue.push("a")
        self.queue.push("b")
        self.queue.pop()
        self.assertEqual(1, self.queue.size())

    def test_single_push(self):
        self.queue.push("a")
        self.assertEqual("[a]", str(self.queue))

    def test_multiple_push(self):
        self.queue.push("a")
        self.queue.push("b")
        self.assertEqual("[a, b]", str(self.queue))

    def test_peek_empty(self):
        self.assertIsNone(self.queue.peek())

    def test_peek_after_push(self):
        self.queue.push("a")
        self.assertEqual("a", self.queue.peek())

    def test_pop_empty(self):
        self.assertIsNone(self.queue.pop())

    def test_pop_single(self):
        self.queue.push("a")
        self.assertEqual("a", self.queue.pop())
        self.assertEqual(0, self.queue.size())

    def test_push_above_capacity(self):
        queue = ArrayQueue(initial_capacity=2)

        queue.push("a")
        queue.push("b")
        queue.push("c")

        self.assertEqual("[a, b, c]", str(queue))

    def test_push_pop_above_capacity_and_back(self):
        queue = ArrayQueue(initial_capacity=2)

        queue.push("a")
        queue.push("b")
        queue.push("c")
        queue.push("d")

        queue.pop()
        queue.pop()
        queue.pop()

        queue.push("e")
        queue.push("f")

        self.assertEqual("[d, e, f]", str(queue))