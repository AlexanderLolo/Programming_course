import unittest
from problemset_8 import SumOfThe
import random

class Problem8_test(unittest.TestCase):

    def test_regression(self):
        for _ in range(2):
            list1 = [random.randint(-100,100) for i in range(5)]
            sum_list = sum(list1)
            list1.append(sum_list)
            random.shuffle(list1)
            self.assertEqual(SumOfThe(100, list1), sum_list)

if __name__ == "__main__":
    unittest.main()
    