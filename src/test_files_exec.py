import unittest
import random
from files_exec import sum_in_files as summ

class test_files(unittest.TestCase):

    def test_regression(self):
        for i in range(2):
            name = str(i+100) + ".txt"
            with open(name, "w") as f:
                for j in range(3):
                    f.write(str(j) + "\n")
        
        self.assertEqual(summ(100, 101, "./"), 6 )


if __name__ == "__main__":
    unittest.main()
