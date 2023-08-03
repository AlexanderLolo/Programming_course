import unittest
from problemset_4 import Palindrom


class Palindrom_test(unittest.TestCase):

    def test_random(self):

        self.assertEqual(Palindrom(""), True)
        self.assertEqual(Palindrom("1"), True)
        self.assertEqual(Palindrom("11"), True)
        self.assertEqual(Palindrom("12"), False)
        self.assertEqual(Palindrom("121"), True)
        self.assertEqual(Palindrom("123"), False)
        self.assertEqual(Palindrom("1221"), True)
        self.assertEqual(Palindrom("1222"), False)


if __name__ == "__main__":
    unittest.main()