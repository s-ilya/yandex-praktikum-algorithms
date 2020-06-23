from unittest import TestCase, skip
from random import choice, randrange

from sprint_1.array_deque import ArrayDeque, ArrayDequeExceedsCapacity


class ArrayDequeTest(TestCase):
    def setUp(self) -> None:
        self.deque = ArrayDeque()

    def test_push_back(self):
        self.deque.push_back(1)
        self.deque.push_back(2)
        self.assertEqual("[1, 2]", str(self.deque))
        self.assertEqual(2, self.deque.size())

    def test_push_back_exceeds_capacity(self):
        deque = ArrayDeque(2)

        deque.push_back(1)
        deque.push_back(2)
        with self.assertRaises(ArrayDequeExceedsCapacity):
            deque.push_back(3)

    def test_pop_front(self):
        self.deque.push_back(1)
        self.deque.push_back(2)

        self.assertEqual(1, self.deque.pop_front())
        self.assertEqual(2, self.deque.pop_front())
        self.assertEqual(0, self.deque.size())

    def test_push_front(self):
        self.deque.push_front(1)
        self.deque.push_front(2)

        self.assertEqual("[2, 1]", str(self.deque))
        self.assertEqual(2, self.deque.size())

    def test_pop_back(self):
        self.deque.push_back(1)
        self.deque.push_back(2)

        self.assertEqual(2, self.deque.pop_back())
        self.assertEqual(1, self.deque.pop_back())

    def test_combined_front_and_back_operations(self):
        deque = ArrayDeque(6)

        deque.push_front(1)
        deque.push_front(2)
        deque.push_front(3)

        self.assertEqual("[3, 2, 1]", str(deque))
        self.assertEqual(1, deque.pop_back())
        self.assertEqual(2, deque.pop_back())
        self.assertEqual(3, deque.pop_back())

        deque.push_front(4)
        deque.push_front(5)
        deque.push_back(6)
        deque.push_back(7)

        self.assertEqual("[5, 4, 6, 7]", str(deque))

    def test_bug(self):
        deque = ArrayDeque(2)
        deque.push_front(1)
        deque.push_front(2)

        with self.assertRaises(ArrayDequeExceedsCapacity):
            deque.push_front(3)

        self.assertEqual("[2, 1]", str(deque))

    def test_random(self):
        commands = ['push_back', 'push_front', 'pop_back', 'pop_front']

        for _ in range(900):
            capacity = randrange(10)
            commands_n = randrange(200)
            commands_history = list()

            deque = ArrayDeque(capacity)

            try:
                for n in range(commands_n):
                    command = choice(commands)

                    if command == 'push_back':
                        commands_history.append(command + ' ' + str(n))
                        try:
                            deque.push_back(n)
                        except ArrayDequeExceedsCapacity:
                            pass
                    elif command == 'push_front':
                        commands_history.append(command + ' ' + str(n))
                        try:
                            deque.push_front(n)
                        except ArrayDequeExceedsCapacity:
                            pass
                    elif command == 'pop_front':
                        commands_history.append(command)
                        deque.pop_front()
                    elif command == 'pop_back':
                        commands_history.append(command)
                        deque.pop_back()
            except Exception as e:
                print(e)
                print(capacity)
                print(commands_history)
