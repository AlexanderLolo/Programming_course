import unittest
from problemset_11_bloomfilter import BloomFilter


class BloomFilter_test(unittest.TestCase):

    def test_regression(self):
        filter = BloomFilter(32)
        self.assertEqual(filter.hash1("c"), 2 ** 3)
        self.assertEqual(filter.hash1("cc"), 2 ** 22)
        self.assertEqual(filter.hash2("cc"), 2 ** 0)

        a = "0123456789"
        filter = BloomFilter(32)

        for i in range(10):
            a = a[i:] + a[:i]
            filter.add(a)
            self.assertEqual(filter.is_value(a), True)


if __name__ == "__main__":
    unittest.main()
