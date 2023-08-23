import unittest
from problemset_7 import matrix


class matrix_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(matrix(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ]), [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
        self.assertEqual(matrix(1, 4, [[1], [5], [9], [13]]), [1, 5, 9, 13])
        self.assertEqual(matrix(4, 1, [[1, 2, 3, 4]]), [1, 2, 3, 4])
        self.assertEqual(matrix(3, 4, [[1, 2, 3], [5, 6, 7], [9, 10, 11], [13, 14, 15]]), [1, 2, 3, 7, 11, 15, 14, 13, 9, 5, 6, 10])
        self.assertEqual(matrix(4, 3, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), [1, 2, 3, 4, 8, 12, 11, 10, 9,5, 6, 7])
        self.assertEqual(matrix(2, 2, [[1, 2], [3, 4]]), [1, 2, 4, 3])

if __name__ == "__main__":
    unittest.main()
