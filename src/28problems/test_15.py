import unittest
from problemset_15 import TankRush


class Problem15_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 3, 2, "23 34 98"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 1, "2 3"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 1, "5 7"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 4, "1234 2345"), True)
        self.assertEqual(TankRush(0, 0, "", 0, 0, ""), True)
        self.assertEqual(TankRush(3,3, '321 694 798', 2, 2, '69 98'), False)


        
if __name__ == "__main__":
    unittest.main()
