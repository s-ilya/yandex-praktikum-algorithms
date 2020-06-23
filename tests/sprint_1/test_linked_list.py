from unittest import TestCase

from sprint_1.linked_list import LinkedList


class TestLinkedList(TestCase):
    def setUp(self) -> None:
        self.linkedList = LinkedList()

    def test_new_list_is_empty(self):
        self.assertTrue(self.linkedList.is_empty())

    def test_print_empty(self):
        self.assertEqual("[]", str(self.linkedList))

    def test_append_one(self):
        self.linkedList.append("a")
        self.assertEqual("[a]", str(self.linkedList))

    def test_append_two(self):
        self.linkedList.append("a")
        self.linkedList.append("b")
        self.assertEqual("[a, b]", str(self.linkedList))

    def test_reverse_empty(self):
        self.assertEqual("[]", str(self.linkedList.reversed()))

    def test_reverse_single(self):
        self.linkedList.append("a")
        self.assertEqual("[a]", str(self.linkedList.reversed()))

    def test_reverse_two(self):
        self.linkedList.append("a")
        self.linkedList.append("b")
        self.assertEqual("[b, a]", str(self.linkedList.reversed()))

    def test_reverse_not_change_original(self):
        self.linkedList.append("a")
        self.linkedList.append("b")
        self.linkedList.reversed()
        self.assertEqual("[a, b]", str(self.linkedList))

    def test_insert_single(self):
        self.linkedList.insert("a")
        self.assertEqual("[a]", str(self.linkedList))

    def test_insert_two(self):
        self.linkedList.insert("a")
        self.linkedList.insert("b")
        self.assertEqual("[b, a]", str(self.linkedList))

    def test_insert_before(self):
        self.linkedList.insert("a")
        self.linkedList.insert("b", before=1)
        self.assertEqual("[a, b]", str(self.linkedList))

    def test_insert_before_out_of_bounds_negative(self):
        self.linkedList.insert("a", before=-1)
        self.assertEqual("[a]", str(self.linkedList))

    def test_insert_before_out_of_bounds_positive(self):
        self.linkedList.insert("a", before=100)
        self.assertEqual("[a]", str(self.linkedList))

    def test_first_after_append(self):
        self.linkedList.append("a")
        self.assertEqual("a", self.linkedList.first().value)

    def test_first_after_single_insert(self):
        self.linkedList.insert("a")
        self.assertEqual("a", self.linkedList.first().value)

    def test_first_after_multiple_inserts(self):
        self.linkedList.insert("a")
        self.linkedList.insert("b")
        self.assertEqual("b", self.linkedList.first().value)

    def test_can_pop_from_empty(self):
        value = self.linkedList.pop()
        self.assertIs(None, value)

    def test_pop_first_from_single(self):
        self.linkedList.append("a")
        value = self.linkedList.pop()

        self.assertEqual("a", value)
        self.assertTrue(self.linkedList.is_empty())

    def test_pop_first_from_multiple(self):
        self.linkedList.append("a")
        self.linkedList.append("b")

        value = self.linkedList.pop()
        self.assertEqual("a", value)

        value = self.linkedList.pop()
        self.assertEqual("b", value)

        self.assertTrue(self.linkedList.is_empty())

    def test_pop_last(self):
        self.linkedList.append("a")
        self.linkedList.append("b")

        value = self.linkedList.pop(index=1)
        self.assertEqual("b", value)
        self.assertEqual("[a]", str(self.linkedList))

    def test_pop_middle(self):
        self.linkedList.append("a")
        self.linkedList.append("b")
        self.linkedList.append("c")

        value = self.linkedList.pop(1)
        self.assertEqual("b", value)
        self.assertEqual("[a, c]", str(self.linkedList))

    def test_find_empty(self):
        self.assertEqual(-1, self.linkedList.find_index("a"))

    def test_find_not_exists(self):
        self.linkedList.append("a")
        self.assertEqual(-1, self.linkedList.find_index("b"))

    def test_find_single(self):
        self.linkedList.append("a")
        self.assertEqual(0, self.linkedList.find_index("a"))

    def test_find_first(self):
        self.linkedList.append("a")
        self.linkedList.append("b")
        self.linkedList.append("c")
        self.assertEqual(0, self.linkedList.find_index("a"))

    def test_find_middle(self):
        self.linkedList.append("a")
        self.linkedList.append("b")
        self.linkedList.append("c")
        self.assertEqual(1, self.linkedList.find_index("b"))

    def test_find_last(self):
        self.linkedList.append("a")
        self.linkedList.append("b")
        self.linkedList.append("c")
        self.assertEqual(2, self.linkedList.find_index("c"))