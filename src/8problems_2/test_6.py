import unittest
from problemset_6 import TRC_sort


class sort_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TRC_sort([1, 1, 0, 0, 2, 0, 0]), [0, 0, 0, 0, 1, 1, 2])
        self.assertEqual(TRC_sort([1]), [1])
        self.assertEqual(TRC_sort([0]), [0])
        self.assertEqual(TRC_sort([2]), [2])
        self.assertEqual(TRC_sort([2, 1, 0]), [0, 1, 2])
        self.assertEqual(TRC_sort([0, 1, 2, 1, 0, 2]), [0, 0, 1, 1, 2, 2])


if __name__ == "__main__":
    unittest.main()
