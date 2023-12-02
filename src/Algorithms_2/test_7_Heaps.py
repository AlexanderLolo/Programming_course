import unittest
from problemset_7_Heap import Heap


class Heap_test(unittest.TestCase):


    def test_all_functions(self):
        test_heap = Heap()
        test_heap.MakeHeap([5,2,7,4,9], 2)
        self.assertEqual(test_heap.GetMax(), 9)
        self.assertEqual(test_heap.GetMax(), 7)
        self.assertEqual(test_heap.GetMax(), 5)
        self.assertEqual(test_heap.GetMax(), 4)
        self.assertEqual(test_heap.GetMax(), 2)
        self.assertEqual(test_heap.GetMax(), -1)

        test_heap.MakeHeap([5,2,7,4], 2)
        self.assertIs(test_heap.Add(9), True)
        self.assertIs(test_heap.Add(6), True)
        self.assertIs(test_heap.Add(9), True)

        self.assertEqual(test_heap.GetMax(), 9)
        self.assertEqual(test_heap.GetMax(), 9)



if __name__ == "__main__":
    unittest.main()
