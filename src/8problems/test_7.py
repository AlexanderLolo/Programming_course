import unittest
from problemset_7 import Secondmax


class Secondmax_test(unittest.TestCase):

    def test_sec(self):

        self.assertEqual(Secondmax([1, 2, 3]), 2)
        self.assertEqual(Secondmax([1, 2]), 1)
        self.assertEqual(Secondmax([2, 2]), 2)
        self.assertEqual(Secondmax([1]), None)
        self.assertEqual(Secondmax([]), None)
        self.assertEqual(Secondmax([1, 1]), 1)
        self.assertEqual(Secondmax([1, 4, 6, 9, 12, 7, 12]), 12)
        self.assertEqual(Secondmax([11, 11, 11, 11, 12, 7, 1]), 11)


if __name__ == "__main__":
    unittest.main()
