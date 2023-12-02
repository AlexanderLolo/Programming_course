import unittest
from problemset_6_Balanced_Trees import BSTNode, BalancedBST


class BinaryTree_test(unittest.TestCase):

    def test_array(self):

        balanced_Tree = BalancedBST()
        input_array = [i for i in range(6,-1,-1)]
        balanced_Tree.GenerateTree(input_array)

        self.assertIs(balanced_Tree.IsCorrect(balanced_Tree.Root), True)
        self.assertIs(balanced_Tree.IsBalanced(balanced_Tree.Root), True)
        self.assertEqual(balanced_Tree.Root.Level, 0)
        self.assertEqual(balanced_Tree.Root.LeftChild.Level, 1)
        self.assertEqual(balanced_Tree.Root.LeftChild.LeftChild.Level, 2)


if __name__ == "__main__":
    unittest.main()
