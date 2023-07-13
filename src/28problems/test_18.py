import unittest
from problemset_18 import MisterRobot


class Problem18_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MisterRobot(7, [1,3,4,5,6,2,7]), True)
        self.assertEqual(MisterRobot(4, [1,2,3,4]), True)
        self.assertEqual(MisterRobot(4, [1,3,2,4]), False)
        self.assertEqual(MisterRobot(4, [3,1,3,4]), True)
        self.assertEqual(MisterRobot(4, [3,1,3,4]), True)


if __name__ == "__main__":
    unittest.main()
