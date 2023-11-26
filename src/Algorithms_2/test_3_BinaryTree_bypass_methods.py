import unittest
from problemset_2_BinaryTree import BSTNode, BST


class BinaryTree_test(unittest.TestCase):

    def setUp(self):
        self.Root = None
        self.BinaryTree = BST(self.Root)

    def test_wide_all_nodes(self):

        self.assertEqual([node.NodeKey for node in self.BinaryTree.WideAllNodes()], [])
        self.Root = BSTNode(8, "8", None)
        self.BinaryTree = BST(self.Root)
        self.assertEqual([node.NodeKey for node in self.BinaryTree.WideAllNodes()], [8])

        self.BinaryTree.AddKeyValue(4, "4")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.WideAllNodes()], [8, 4])
        self.BinaryTree.AddKeyValue(12, "12")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.WideAllNodes()], [8, 4, 12])
        self.BinaryTree.AddKeyValue(2, "2")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.WideAllNodes()], [8, 4, 12, 2])
        self.BinaryTree.AddKeyValue(6, "6")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.WideAllNodes()], [8, 4, 12, 2, 6])
        self.BinaryTree.AddKeyValue(1, "1")
        self.BinaryTree.AddKeyValue(3, "3")
        self.BinaryTree.AddKeyValue(5, "5")
        self.BinaryTree.AddKeyValue(7, "7")
        self.BinaryTree.AddKeyValue(10, "10")
        self.BinaryTree.AddKeyValue(14, "14")
        self.BinaryTree.AddKeyValue(9, "9")
        self.BinaryTree.AddKeyValue(11, "11")
        self.BinaryTree.AddKeyValue(13, "13")
        self.BinaryTree.AddKeyValue(15, "15")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.WideAllNodes()], [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
        self.BinaryTree.AddKeyValue(-1, "-1")
        self.BinaryTree.AddKeyValue(-2, "-2")
        self.BinaryTree.AddKeyValue(-3, "-3")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.WideAllNodes()], [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15, -1, -2, -3])


    def test_in_order_deep_bypass(self):

        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [])
        self.Root = BSTNode(8, "8", None)
        self.BinaryTree = BST(self.Root)
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [8])
        self.BinaryTree.AddKeyValue(4, "4")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [4, 8])
        self.BinaryTree.AddKeyValue(12, "12")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [4, 8, 12])
        self.BinaryTree.AddKeyValue(2, "2")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [2, 4, 8, 12])
        self.BinaryTree.AddKeyValue(6, "6")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [2, 4, 6, 8, 12])
        self.BinaryTree.AddKeyValue(1, "1")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [1, 2, 4, 6, 8, 12])
        self.BinaryTree.AddKeyValue(3, "3")
        self.BinaryTree.AddKeyValue(5, "5")
        self.BinaryTree.AddKeyValue(7, "7")
        self.BinaryTree.AddKeyValue(10, "10")
        self.BinaryTree.AddKeyValue(14, "14")
        self.BinaryTree.AddKeyValue(9, "9")
        self.BinaryTree.AddKeyValue(11, "11")
        self.BinaryTree.AddKeyValue(13, "13")
        self.BinaryTree.AddKeyValue(15, "15")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_post_order_deep_bypass(self):

        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(1)], [])
        self.Root = BSTNode(8, "8", None)
        self.BinaryTree = BST(self.Root)
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(1)], [8])
        self.BinaryTree.AddKeyValue(4, "4")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(1)], [4, 8])
        self.BinaryTree.AddKeyValue(12, "12")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(1)], [4, 12, 8])
        self.BinaryTree.AddKeyValue(2, "2")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(1)], [2, 4, 12, 8])
        self.BinaryTree.AddKeyValue(6, "6")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(1)], [2, 6, 4, 12, 8])
        self.BinaryTree.AddKeyValue(1, "1")
        self.BinaryTree.AddKeyValue(3, "3")
        self.BinaryTree.AddKeyValue(5, "5")
        self.BinaryTree.AddKeyValue(7, "7")
        self.BinaryTree.AddKeyValue(10, "10")
        self.BinaryTree.AddKeyValue(14, "14")
        self.BinaryTree.AddKeyValue(9, "9")
        self.BinaryTree.AddKeyValue(11, "11")
        self.BinaryTree.AddKeyValue(13, "13")
        self.BinaryTree.AddKeyValue(15, "15")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(1)], [1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8])

    def test_pre_order_deep_bypass(self):
        
        self.Root = BSTNode(8, "8", None)
        self.BinaryTree = BST(self.Root)
        self.BinaryTree.AddKeyValue(4, "4")
        self.BinaryTree.AddKeyValue(12, "12")
        self.BinaryTree.AddKeyValue(2, "2")
        self.BinaryTree.AddKeyValue(6, "6")
        self.BinaryTree.AddKeyValue(1, "1")
        self.BinaryTree.AddKeyValue(3, "3")
        self.BinaryTree.AddKeyValue(5, "5")
        self.BinaryTree.AddKeyValue(7, "7")
        self.BinaryTree.AddKeyValue(10, "10")
        self.BinaryTree.AddKeyValue(14, "14")
        self.BinaryTree.AddKeyValue(9, "9")
        self.BinaryTree.AddKeyValue(11, "11")
        self.BinaryTree.AddKeyValue(13, "13")
        self.BinaryTree.AddKeyValue(15, "15")
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(2)], [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])

    def test_invert_binarytree(self):
        
        self.Root = BSTNode(8, "8", None)
        self.BinaryTree = BST(self.Root)
        self.BinaryTree.AddKeyValue(4, "4")
        self.BinaryTree.AddKeyValue(12, "12")
        self.BinaryTree.AddKeyValue(2, "2")
        self.BinaryTree.AddKeyValue(6, "6")
        self.BinaryTree.AddKeyValue(1, "1")
        self.BinaryTree.AddKeyValue(3, "3")
        self.BinaryTree.AddKeyValue(5, "5")
        self.BinaryTree.AddKeyValue(7, "7")
        self.BinaryTree.AddKeyValue(10, "10")
        self.BinaryTree.AddKeyValue(14, "14")
        self.BinaryTree.AddKeyValue(9, "9")
        self.BinaryTree.AddKeyValue(11, "11")
        self.BinaryTree.AddKeyValue(13, "13")
        self.BinaryTree.AddKeyValue(15, "15")
        
        self.BinaryTree.invert_binary_tree()
        self.assertEqual([node.NodeKey for node in self.BinaryTree.DeepAllNodes(0)], [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])


if __name__ == "__main__":
    unittest.main()
