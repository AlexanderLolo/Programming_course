import unittest
from problemset_6 import PatternUnlock 

class Problem6_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(PatternUnlock(1,[4]), "")
        self.assertEqual(PatternUnlock(10, [1,2,3,4,5,6,2,7,8,9]), "982843")


if __name__ == "__main__":
    unittest.main()
    