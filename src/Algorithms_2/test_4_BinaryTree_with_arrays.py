import unittest
from problemset_4_BinaryTree_with_arrays import aBST


class BinaryTree_test(unittest.TestCase):

    def setUp(self):
        self.BinaryTree = aBST(2)

    def test_add_and_search(self):

        self.assertEqual(self.BinaryTree.FindKeyIndex(4), 0)
        self.assertEqual(self.BinaryTree.FindKeyIndex(4), 0)
        self.assertEqual(self.BinaryTree.AddKey(4), 0)

        self.assertEqual(self.BinaryTree.FindKeyIndex(2), -1)
        self.assertEqual(self.BinaryTree.AddKey(2), 1)
        self.assertEqual(self.BinaryTree.AddKey(2), 1)
        self.assertEqual(self.BinaryTree.FindKeyIndex(2), 1)

        self.assertEqual(self.BinaryTree.FindKeyIndex(6), -2)
        self.assertEqual(self.BinaryTree.AddKey(6), 2)
        self.assertEqual(self.BinaryTree.FindKeyIndex(6), 2)
        self.assertEqual(self.BinaryTree.AddKey(1), 3)
        self.assertEqual(self.BinaryTree.AddKey(3), 4)
        self.assertEqual(self.BinaryTree.AddKey(7), 6)
        self.assertEqual(self.BinaryTree.AddKey(5), 5)
        self.assertEqual(self.BinaryTree.AddKey(8), -1)
        self.assertIs(self.BinaryTree.FindKeyIndex(8), None)



if __name__ == "__main__":
    unittest.main()
