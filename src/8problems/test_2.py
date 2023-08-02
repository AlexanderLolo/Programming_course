import unittest
import random
from problemset_2 import Sumofnum


class Sum_test(unittest.TestCase):

    def test_random(self):
        for _ in range(100000):
            M = random.randint(1, 100000000000000000000)
            self.assertEqual(Sumofnum(M), sum(map(int, str(M))))


if __name__ == "__main__":
    unittest.main()