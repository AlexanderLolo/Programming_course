import unittest
from problemset_24 import MatrixTurn


class Problem23_test(unittest.TestCase):

    def test_regression(self):
        a = ["123456", "234567", "345678", "456789"]
        MatrixTurn(a, 6, 4, 2)
        self.assertEqual(a, ["321234", "454345", "567656", "678987"])

        a = ["4321", "5432", "6543", "7654", "8765", "9876"]
        MatrixTurn(a, 4, 6, 1)
        self.assertEqual(a, ["5432", "6541", "7632", "8743", "9654", "8765"])


if __name__ == "__main__":
    unittest.main()
