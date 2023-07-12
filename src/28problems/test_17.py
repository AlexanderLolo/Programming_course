import unittest
from problemset_17 import LineAnalysis


class Problem17_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(LineAnalysis("*..*..*..*..*..*..*"), True)
        self.assertEqual(LineAnalysis("*"), True)
        self.assertEqual(LineAnalysis("**"), True)
        self.assertEqual(LineAnalysis("***"), True)
        self.assertEqual(LineAnalysis("*....*....*"), True)


if __name__ == "__main__":
    unittest.main()
