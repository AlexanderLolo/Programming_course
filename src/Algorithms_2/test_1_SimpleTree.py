import unittest
from ps_1_SimpleTree import SimpleTreeNode, SimpleTree


class SimpleTree_test(unittest.TestCase):

    def setUp(self):
        self.Root = SimpleTreeNode(0, None)
        self.SimpleTree = SimpleTree(self.Root)

        self.Child1 = SimpleTreeNode(1, None)
        self.Child2 = SimpleTreeNode(2, None)
        self.Child3 = SimpleTreeNode(3, None)
        self.Child4 = SimpleTreeNode(3, None)

        self.SimpleTree.AddChild(self.Root, self.Child1)
        self.SimpleTree.AddChild(self.Root, self.Child2)
        self.SimpleTree.AddChild(self.Child2, self.Child3)
        self.SimpleTree.AddChild(self.Root, self.Child4)

    def test_add_child(self):

        self.assertIn(self.Child1, self.Root.Children)
        self.assertIn(self.Child3, self.Child2.Children)
        self.assertEqual(self.Child3.Parent, self.Child2)
        self.assertEqual(self.Child2.Parent, self.Root)

    def test_delete_node(self):

        self.SimpleTree.DeleteNode(self.Child2)
        self.assertNotIn(self.Child2, self.Root.Children)
        self.assertEqual(self.Child2.Parent, None)
        self.assertNotIn(self.Child3, self.Child2.Children)
        self.assertEqual(self.Child3.Parent, None)

    def test_get_all_nodes(self):

        all_nodes = self.SimpleTree.GetAllNodes()
        self.assertIn(self.Root, all_nodes)
        self.assertIn(self.Child1, all_nodes)
        self.assertIn(self.Child2, all_nodes)
        self.assertIn(self.Child3, all_nodes)
        self.assertIn(self.Child4, all_nodes)

        self.assertEqual(len(all_nodes), 5)

    def test_find_nodes_by_val(self):
        target_nodes = self.SimpleTree.FindNodesByValue(3)
        self.assertIn(self.Child3, target_nodes)
        self.assertIn(self.Child4, target_nodes)

        target_nodes = self.SimpleTree.FindNodesByValue(6)
        self.assertAlmostEqual(len(target_nodes), 0)

    def test_move_node(self):
        self.SimpleTree.MoveNode(self.Child2, self.Child4)
        self.assertIn(self.Child2, self.Child4.Children)
        self.assertNotIn(self.Child2, self.Root.Children)
        self.assertEqual(self.Child2.Parent, self.Child4)
        self.assertEqual(self.Child3.Parent, self.Child2)

    def test_count(self):
        self.assertEqual(self.SimpleTree.Count(), 2)
        self.assertEqual(self.SimpleTree.LeafCount(), 3)


if __name__ == "__main__":
    unittest.main()
