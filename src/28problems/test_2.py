import unittest
from problemset_2 import odometer

class problem2test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(odometer([0,0]), 0)
        self.assertEqual(odometer([10,2]), 20)
        self.assertEqual(odometer([0,10]), 0)
        self.assertEqual(odometer([10,0]), 0)
        self.assertEqual(odometer([10,1,20,2]), 30)
        self.assertEqual(odometer([0,1,20,2]), 20)
        self.assertEqual(odometer([0,1,20,1]), 0)
        self.assertEqual(odometer([10,0,20,1]), 20)
        self.assertEqual(odometer([10,1,20,2,30,3]), 60)
        self.assertEqual(odometer([10,1,20,2,30,2]), 30)

if __name__ == "__main__":
    unittest.main()