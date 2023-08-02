import unittest
import random
from math import isclose
from problemset_1 import Power


class Power_test(unittest.TestCase):

    def test_random(self):
        for _ in range(100):
            M = random.randint(-50, 50)
            N = random.randint(-50, -1)

            self.assertEqual(isclose(Power(N, M), (N ** M)), True)
            self.assertEqual(isclose(Power(-N, M), ((-N) ** M)), True)
            self.assertEqual(Power(0, 0), 0 ** 0)


if __name__ == "__main__":
    unittest.main()