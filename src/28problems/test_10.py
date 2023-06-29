import unittest
from problemset_10 import PrintingCosts


class Problem10_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(PrintingCosts(""), 0)
        self.assertEqual(PrintingCosts("         "), 0)
        self.assertEqual(PrintingCosts("     z t    "), 36)
        self.assertEqual(PrintingCosts("     z t ф ф ф  "), 105)

if __name__ == "__main__":
    unittest.main()
