import unittest
from problemset_16 import MaximumDiscount


class Problem16_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100]), 450)
        self.assertEqual(MaximumDiscount(7, [400, 350, 300, 250, 200, 150]), 450)
        self.assertEqual(MaximumDiscount(0, []), 0)
        self.assertEqual(MaximumDiscount(2, [1, 2]), 0)


if __name__ == "__main__":
    unittest.main()
