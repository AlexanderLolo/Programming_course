import unittest
from problemset_9 import TheRabbitsFoot


class Problem9_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TheRabbitsFoot("", True), "")
        self.assertEqual(TheRabbitsFoot("", False), "")
        self.assertEqual(TheRabbitsFoot("123456789", True), "147 258 369")
        self.assertEqual(TheRabbitsFoot("12345678", True), "147 258 36")
        self.assertEqual(TheRabbitsFoot("1234567", True), "147 25 36")
        self.assertEqual(TheRabbitsFoot("123456", True), "14 25 36")
        self.assertEqual(TheRabbitsFoot("12345", True), "14 25 3")

        self.assertEqual(TheRabbitsFoot("147 258 369", False), "123456789")
        self.assertEqual(TheRabbitsFoot("147 258 36", False), "12345678")
        self.assertEqual(TheRabbitsFoot("147 25 36", False), "1234567")
        self.assertEqual(TheRabbitsFoot("14 25 36", False), "123456")
        self.assertEqual(TheRabbitsFoot("14 25 3", False), "12345")


if __name__ == "__main__":
    unittest.main()
