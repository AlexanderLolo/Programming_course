import unittest
from problemset_12_cache import NativeCache


class NativeCache_test(unittest.TestCase):

    def test_regression(self):
        nativecache = NativeCache(19)
        self.assertEqual(nativecache.get("1"), None)
        nativecache.put("1", 2)
        self.assertEqual(nativecache.get("1"), 2)
        self.assertEqual(nativecache.get("1"), 2)
        self.assertEqual(nativecache.hits[nativecache.find("1")], 2)

        nativecache.put("1", 2)
        self.assertEqual(nativecache.get("1"), 2)
        self.assertEqual(nativecache.hits[nativecache.find("1")], 3)

        nativecache = NativeCache(19)
        for i in range(19):
            nativecache.put(str(i), i)
            for j in range(i):
                nativecache.get(str(i))


if __name__ == "__main__":
    unittest.main()
