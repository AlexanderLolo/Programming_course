import unittest
from problemset_6_deque import Deque, palindrom


class Deque_test(unittest.TestCase):

    def test_regression_operations_deque(self):
        deque = Deque()
        deque.addFront(1)
        self.assertEqual(deque.queue.head.value, 1)
        self.assertEqual(deque.size(), 1)
        deque.addTail("1")
        self.assertEqual(deque.queue.tail.value, "1")
        self.assertEqual(deque.size(), 2)
        deque.addTail("2")
        self.assertEqual(deque.queue.tail.value, "2")
        self.assertEqual(deque.size(), 3)

        self.assertEqual(deque.removeTail(), "2")
        self.assertEqual(deque.size(), 2)
        self.assertEqual(deque.removeFront(), 1)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.removeFront(), "1")
        self.assertEqual(deque.size(), 0)
        self.assertEqual(deque.removeFront(), None)
        self.assertEqual(deque.size(), 0)

    def test_regression_palindrom(self):
        self.assertEqual(palindrom(""), True)
        self.assertEqual(palindrom("1"), True)
        self.assertEqual(palindrom("11"), True)
        self.assertEqual(palindrom("12"), False)
        self.assertEqual(palindrom("121"), True)
        self.assertEqual(palindrom("1221"), True)


if __name__ == "__main__":
    unittest.main()
