import unittest
from problemset_5 import massdriver


class driver_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(massdriver([1,2,3,4,2,3,1]), 0)
        self.assertEqual(massdriver([1,2,3,1,2,3,4]), 0)
        self.assertEqual(massdriver([1,2,3,4,3,4,2]), 1)
        self.assertEqual(massdriver([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]), -1)


if __name__ == "__main__":
    unittest.main()
