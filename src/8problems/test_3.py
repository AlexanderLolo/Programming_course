import unittest
import random
from problemset_3 import Listlen


class Len_test(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            M = random.randint(1, 500)
            self.assertEqual(Listlen([1] * M), len([1] * M))
            self.assertEqual(Listlen([]), 0)


if __name__ == "__main__":
    unittest.main()