import unittest
from problemset_21 import BiggerGreater


class Problem21_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(BiggerGreater("12345"), "12354")
        self.assertEqual(BiggerGreater("1"), "")
        self.assertEqual(BiggerGreater("нклм"), "нкмл")
        self.assertEqual(BiggerGreater("вибк"), "викб")
        self.assertEqual(BiggerGreater("вкиб"), "ибвк")


if __name__ == "__main__":
    unittest.main()
