import unittest
import random
from problemset_11 import BigMinus


class Problem11_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(BigMinus("", "1"), "1")
        self.assertEqual(BigMinus("9", "10"), "1")

        for _ in range(100000):
            a = random.randint(0, 100)
            b = random.randint(0, 100)
            self.assertEqual(BigMinus(str(a), str(b)), str(abs(a-b)))


if __name__ == "__main__":
    unittest.main()
