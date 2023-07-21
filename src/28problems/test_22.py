import unittest
from problemset_22 import SherlockValidString


class Problem22_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(SherlockValidString("xyz"), True)
        self.assertEqual(SherlockValidString("xyzaa"), True)
        self.assertEqual(SherlockValidString("xyzzz"), False)
        self.assertEqual(SherlockValidString("xxyyza"), False)
        self.assertEqual(SherlockValidString("xxyyzabc"), False)


if __name__ == "__main__":
    unittest.main()
