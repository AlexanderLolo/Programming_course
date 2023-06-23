import unittest
import problemset_4

class Problem4_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(problemset_4.MadMax(1,[7]) , [7])
        self.assertEqual(problemset_4.MadMax(7,[1,2,3,4,5,6,7]) , [1,2,3,7,6,5,4])
        self.assertEqual(problemset_4.MadMax(7,[7,4,6,3,5,2,1]) , [1,2,3,7,6,5,4])
        self.assertEqual(problemset_4.MadMax(5,[1,2,3,4,5]) , [1,2,5,4,3])
        self.assertEqual(problemset_4.MadMax(9,[7,4,6,3,5,2,1,8,9]) , [1,2,3,4,9,8,7,6,5])

if __name__ == "__main__":
    unittest.main()
    