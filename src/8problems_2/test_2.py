import unittest
from problemset_2 import digital_rain


class digital_test(unittest.TestCase):

    def test_regression(self):

        self.assertEqual(digital_rain("1111000"), "111000")
        self.assertEqual(digital_rain("11101000"), "11101000")
        self.assertEqual(digital_rain("011111110"), "10")
        self.assertEqual(digital_rain("1111111"), "")
        self.assertEqual(digital_rain(""), "")


if __name__ == "__main__":
    unittest.main()