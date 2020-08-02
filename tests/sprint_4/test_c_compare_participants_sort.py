from unittest import TestCase

from sprint_4.c_heap_sort import compare_participants, Participant, heap_sort


class TestCompareParticipants(TestCase):
    def test_two_kondtraty(self):
        self.assertEqual(
            1,
            compare_participants(
                Participant('nekondratiy', [99], 1),
                Participant('drkonxxxiyatt', [1], 2)
            )
        )

    def test_by_positive_points(self):
        self.assertTrue(
            compare_participants(
                Participant('a', [-1000, 99]),
                Participant('b', [50])
            ) < 0
        )

    def test_by_names(self):
        self.assertEqual(
            1,
            compare_participants(
                Participant('b', [1]),
                Participant('a', [1])
            )
        )

    def test_equal(self):
        self.assertEqual(
            0,
            compare_participants(
                Participant('a', [1]),
                Participant('a', [1])
            )
        )

    def test_priorities_were_unordered(self):
        one = Participant('a', [1], 1)
        two = Participant('a', [1], 2)

        self.assertEqual(
            [two, one],
            heap_sort(
               [one, two], compare_participants
            )
        )

    def test_priorities_were_in_order(self):
        one = Participant('a', [1], 1)
        two = Participant('a', [1], 2)

        self.assertEqual(
            [two, one],
            heap_sort(
               [one, two], compare_participants
            )
        )