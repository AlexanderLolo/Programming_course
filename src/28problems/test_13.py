import unittest
import random
from problemset_13 import UFO


class Problem13_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(UFO(2, [1234, 1777], False), [4660, 6007])
        self.assertEqual(UFO(2, [1234, 1777], True), [668, 1023])
        self.assertEqual(UFO(1, [0], True), [0])
        self.assertEqual(UFO(1, [97], False), [151])

        for _ in range(100000):
            a = random.randint(1, 1000)
            self.assertEqual(UFO(1, [oct(a)], True), [a])
            self.assertEqual(UFO(1, [hex(a)], False), [a])


if __name__ == "__main__":
    unittest.main()
