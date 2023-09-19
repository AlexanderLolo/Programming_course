import unittest
from problemset_8_hashtables import HashTable


class Hashtable_test(unittest.TestCase):

    def test_regression(self):
        hashtable = HashTable(17, 3)
        self.assertEqual(hashtable.find("18"), None)
        a = []
        for i in range(17):
            a.append(hashtable.put(str(i)))
        self.assertEqual(hashtable.put(str(17)), None)

        for i, element in enumerate(a):
            self.assertEqual(hashtable.find(str(i)), element)
        self.assertEqual(hashtable.find("18"), None)


if __name__ == "__main__":
    unittest.main()
