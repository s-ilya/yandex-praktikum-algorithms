from unittest import TestCase

from sprint_1.list_queue import ListQueue, ListQueueEmptyError


class ListQueueTest(TestCase):
    def setUp(self) -> None:
        self.queue = ListQueue()

    def test_size_new(self):
        self.assertEqual(0, self.queue.size())

    def test_size_put(self):
        self.queue.put("a")
        self.assertEqual(1, self.queue.size())

    def test_size_get(self):
        self.queue.put("a")
        self.queue.put("b")
        self.queue.get()
        self.assertEqual(1, self.queue.size())

    def test_single_put(self):
        self.queue.put("a")
        self.assertEqual("[a]", str(self.queue))

    def test_multiple_put(self):
        self.queue.put("a")
        self.queue.put("b")
        self.assertEqual("[a, b]", str(self.queue))

    def test_get_empty(self):
        with self.assertRaises(ListQueueEmptyError):
            self.queue.get()

    def test_get_single(self):
        self.queue.put("a")
        self.assertEqual("a", self.queue.get())
        self.assertEqual(0, self.queue.size())

    def test_get_multiple(self):
        self.queue.put("a")
        self.queue.put("b")
        self.assertEqual("a", self.queue.get())
        self.assertEqual("b", self.queue.get())
        self.assertEqual(0, self.queue.size())
