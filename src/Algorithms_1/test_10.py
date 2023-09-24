import unittest
from problemset_10_powerset import PowerSet


class PowerSet_test(unittest.TestCase):

    def test_regression(self):
        aset = PowerSet()
        aset.put("1")
        self.assertEqual(list(aset.slots.keys())[0], "1")
        self.assertEqual(aset.size(), 1)
        aset.put("1")
        self.assertEqual(aset.size(), 1)
        aset.remove("1")
        self.assertEqual(aset.size(), 0)
        aset.remove("1")
        self.assertEqual(aset.size(), 0)

        bset = PowerSet()
        aset.union(bset)
        self.assertEqual(aset.size(), 0)
        bset.put("1")
        aset.union(bset)
        self.assertEqual(aset.size(), 1)
        bset.put("2")
        aset.union(bset)
        self.assertEqual(aset.size(), 2)
        bset = PowerSet()
        aset.union(bset)
        self.assertEqual(aset.size(), 2)

        bset = PowerSet()
        aset = PowerSet()
        aset.intersection(bset)
        self.assertEqual(aset.size(), 0)
        bset.put("1")
        aset.intersection(bset)
        self.assertEqual(aset.size(), 0)
        aset.put("1")
        aset.intersection(bset)
        self.assertEqual(aset.size(), 1)
        bset.put("2")
        aset.intersection(bset)
        self.assertEqual(aset.size(), 1)

        aset.difference(bset)
        self.assertEqual(aset.size(), 0)
        aset.put("3")
        aset.difference(bset)
        self.assertEqual(aset.size(), 1)

        bset = PowerSet()
        bset.put("1")
        self.assertEqual(aset.issubset(bset), False)
        aset.put("1")
        self.assertEqual(aset.issubset(bset), True)
        bset.put("3")
        self.assertEqual(aset.issubset(bset), True)
        bset.put("4")
        self.assertEqual(aset.issubset(bset), False)

        for i in range(30000):
            bset.put(str(i))

        for i in range(30000):
            aset.put(str(i+1))

        aset.intersection(bset)
        self.assertEqual(aset.size(), 29999)

        aset.union(bset)
        self.assertEqual(aset.size(), 30000)


if __name__ == "__main__":
    unittest.main()
