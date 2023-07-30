import unittest
from problemset_27 import Football


class Problem27_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(Football([1, 3, 2], 3), True)
        self.assertEqual(Football([1], 1), False)
        self.assertEqual(Football([1, 2, 3], 3), False)
        self.assertEqual(Football([3, 1, 1], 3), True)
        self.assertEqual(Football([1, 7, 5, 3, 9], 5), True)
        self.assertEqual(Football([9, 5, 3, 7, 1], 5), False)
        self.assertEqual(Football([1, 4, 3, 2, 5], 5), True)


if __name__ == "__main__":
    unittest.main()
