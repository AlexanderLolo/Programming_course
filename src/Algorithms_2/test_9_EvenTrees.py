import unittest
from problemset_9_even_trees import SimpleTreeNode, SimpleTree


class SimpleTree_test(unittest.TestCase):

    def setUp(self):
        self.Root = SimpleTreeNode(1, None)
        self.SimpleTree = SimpleTree(self.Root)
        self.Child2 = SimpleTreeNode(2, None)
        self.Child3 = SimpleTreeNode(3, None)
        self.Child10 = SimpleTreeNode(10, None)
        self.Child4 = SimpleTreeNode(4, None)
        self.Child5 = SimpleTreeNode(5, None)
        self.Child6 = SimpleTreeNode(6, None)
        self.Child7 = SimpleTreeNode(7, None)
        self.Child8 = SimpleTreeNode(8, None)
        self.Child9 = SimpleTreeNode(9, None)

        self.SimpleTree.AddChild(self.Root, self.Child2)
        self.SimpleTree.AddChild(self.Root, self.Child3)
        self.SimpleTree.AddChild(self.Root, self.Child6)
        self.SimpleTree.AddChild(self.Child2, self.Child5)
        self.SimpleTree.AddChild(self.Child2, self.Child7)
        self.SimpleTree.AddChild(self.Child3, self.Child4)
        self.SimpleTree.AddChild(self.Child6, self.Child8)
        self.SimpleTree.AddChild(self.Child8, self.Child9)
        self.SimpleTree.AddChild(self.Child8, self.Child10)

    def test_even_trees(self):

        list_of_nodes = self.SimpleTree.EvenTrees()

        self.assertEqual(len(list_of_nodes), 4)
        for node in list_of_nodes:
            self.assertTrue(node in [self.Root, self.Child3, self.Child6])
        self.assertIs(list_of_nodes[0], self.Root)
        self.assertIs(list_of_nodes[2], self.Root)

if __name__ == "__main__":
    unittest.main()
