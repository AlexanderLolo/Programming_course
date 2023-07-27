import unittest
from problemset_25 import TransformTransform


class Problem25_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TransformTransform([1, 2, 3, 4], 4), False)
        self.assertEqual(TransformTransform([2], 1), True)


if __name__ == "__main__":
    unittest.main()
