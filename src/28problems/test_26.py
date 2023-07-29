import unittest
from problemset_26 import white_walkers


class Problem26_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(white_walkers("axxb6===4xaf5===eee5"), True)
        self.assertEqual(white_walkers("5==ooooooo=5=5"), False)
        self.assertEqual(white_walkers("abc=7==hdjs=3gg1=======5"), True)
        self.assertEqual(white_walkers("aaS=8"), False)
        self.assertEqual(white_walkers("9===1===9===1===9"), True)
        
if __name__ == "__main__":
    unittest.main()
