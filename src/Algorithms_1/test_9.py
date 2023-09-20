import unittest
from problemset_9_native_dictionaries import NativeDictionary


class NativeDictionary_test(unittest.TestCase):

    def test_regression(self):
        nativedict = NativeDictionary(17)
        self.assertEqual(nativedict.get("1"), None)
        nativedict.put("1", 2)
        self.assertEqual(nativedict.get("1"), 2)
        self.assertEqual(nativedict.get("1"), 2)
        nativedict.put("1", 2)
        self.assertEqual(nativedict.get("1"), 2)
        nativedict.put("1", 3)
        self.assertEqual(nativedict.get("1"), 3)
        self.assertEqual(nativedict.get("2"), None)
        self.assertEqual(nativedict.is_key("1"), True)
        self.assertEqual(nativedict.is_key("2"), False)


if __name__ == "__main__":
    unittest.main()
