import unittest
import problemset_5 as p5

class Problem5_test(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(p5.SynchronizingTables(3, [50, 1, 1024], [20000, 100000, 90000]), [90000, 20000, 100000])
        self.assertEqual(p5.SynchronizingTables(4, [50, 1, 1024, 16, 120000], [20000, 100000, 90000, 13, 800]), [20000, 13, 90000, 800, 100000])
        self.assertEqual(p5.SynchronizingTables(0, [], []), [])
        self.assertEqual(p5.SynchronizingTables(1, [20], [3000]), [3000])

if __name__ == "__main__":
    unittest.main()
    