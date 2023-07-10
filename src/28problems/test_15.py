import unittest
from problemset_15 import TankRush


class Problem15_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "12 23"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "45 87"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 1, 1, "45"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 1, 1, ""), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 3, 4, "1234 2345 0985"), False)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "1234 0987"), True)
        self.assertEqual(TankRush(0, 0, "", 0, 0, ""), True)
        

if __name__ == "__main__":
    unittest.main()
