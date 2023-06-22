import unittest
import random
from problemset_1 import squirrel
import math

class Squirrel_test(unittest.TestCase):

    def test_random(self):
        for i in range(100):
            rand = random.randint(0, 10000)
            rand_string = str(math.factorial(rand))

            self.assertEqual(int(rand_string[0]), squirrel(rand))

    def test_edge(self):
        self.assertEqual(1, squirrel(0))

if __name__ == "__main__":
    unittest.main()