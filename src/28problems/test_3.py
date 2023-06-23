import unittest
import random
from problemset_3 import ConquestCampaign

class Problem3_test(unittest.TestCase):

    def test_no_exceptions(self):
        for _ in range(500):
            self.assertIsNotNone(ConquestCampaign(5,4,1, [random.randint(1,5),random.randint(1,4)]))
    
    def test_regression(self):
        self.assertEqual(ConquestCampaign(0,4,1, [0,1]) , 1)
        self.assertEqual(ConquestCampaign(3,4,2, [2,2, 3,4]), 3)
        self.assertEqual(ConquestCampaign(3,4,3, [3,4, 3,4, 3,4]), 6)
        self.assertEqual(ConquestCampaign(3,4,1, [3,4]), 6)
        self.assertEqual(ConquestCampaign(1,1,1, [1,1]), 1)
        self.assertEqual(ConquestCampaign(1,1,2, [1,1,1,1]), 1)

if __name__ == "__main__":
    unittest.main()