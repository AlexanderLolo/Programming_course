import unittest
from problemset_4_1 import artificial_muscle_fibers


class Art_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 4, 5]), 0)
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 2, 1]), 2)
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 2, 1, 2, 4, 2, 1]), 2)


if __name__ == "__main__":
    unittest.main()
