import unittest
from problemset_14 import Unmanned


class Problem14_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]), 12)
        self.assertEqual(Unmanned(10, 3, [[3, 5, 5], [5, 2, 2], [6, 2, 2]]), 14)
        self.assertEqual(Unmanned(10, 3, [[3, 5, 5], [5, 2, 2], [6, 1, 1]]), 13)
        self.assertEqual(Unmanned(10, 3, [[3, 5, 5], [5, 2, 2], [6, 1, 2]]), 12)
        self.assertEqual(Unmanned(10, 0, []), 10)
        self.assertEqual(Unmanned(1, 0, []), 1)
        self.assertEqual(Unmanned(3, 1, [[3, 5, 5]]), 3)
        self.assertEqual(Unmanned(10, 2, [[11, 5, 5], [15, 2, 2]]), 10)
        self.assertEqual(Unmanned(10, 3, [[3, 5, 5], [5, 2, 2], [11, 5, 5]]), 12)
        self.assertEqual(Unmanned(4, 1, [[3, 5, 5]]), 6)
        self.assertEqual(Unmanned(4, 2, [[3, 5, 5], [5, 2, 2]]), 6)


if __name__ == "__main__":
    unittest.main()
