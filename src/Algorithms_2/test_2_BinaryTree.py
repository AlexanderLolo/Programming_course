import unittest
from problemset_2_BinaryTree import BSTNode, BST


class BinaryTree_test(unittest.TestCase):

    def setUp(self):
        self.Root = BSTNode(100, "value 100", None)
        self.BinaryTree = BST(self.Root)


    def test_Find_and_Add_key_Value(self):
        search_result = self.BinaryTree.FindNodeByKey(100)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertEqual(search_result.Node.NodeKey, 100)

        # тестируем добавление левого узла
        search_result = self.BinaryTree.FindNodeByKey(50)
        self.assertIs(search_result.NodeHasKey, False)

        self.BinaryTree.AddKeyValue(50, "value 50")
        search_result = self.BinaryTree.FindNodeByKey(50)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertIs(self.Root.LeftChild, search_result.Node)

        # тестируем добавление правого узла
        search_result = self.BinaryTree.FindNodeByKey(200)
        self.assertIs(search_result.NodeHasKey, False)

        self.BinaryTree.AddKeyValue(200, "value 200")
        search_result = self.BinaryTree.FindNodeByKey(200)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertIs(self.Root.RightChild, search_result.Node)

        # тестируем добавление узла, который уже есть
        self.assertIs(self.BinaryTree.AddKeyValue(200, "value 200"), False)

    def test_Find_node_by_key(self):
        self.BinaryTree.AddKeyValue(50, "value 50")
        self.BinaryTree.AddKeyValue(200, "value 200")
        self.BinaryTree.AddKeyValue(150, "value 150")
        self.BinaryTree.AddKeyValue(300, "value 300")
        self.BinaryTree.AddKeyValue(25, "value 25")
        self.BinaryTree.AddKeyValue(75, "value 75")
        self.BinaryTree.AddKeyValue(400, "value 400")

        search_result = self.BinaryTree.FindNodeByKey(100)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertEqual(search_result.Node.NodeKey, 100)

        search_result = self.BinaryTree.FindNodeByKey(50)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertEqual(search_result.Node.NodeKey, 50)

        search_result = self.BinaryTree.FindNodeByKey(200)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertEqual(search_result.Node.NodeKey, 200)

        search_result = self.BinaryTree.FindNodeByKey(150)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertEqual(search_result.Node.NodeKey, 150)

        search_result = self.BinaryTree.FindNodeByKey(300)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertEqual(search_result.Node.NodeKey, 300)

        search_result = self.BinaryTree.FindNodeByKey(25)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertEqual(search_result.Node.NodeKey, 25)

        search_result = self.BinaryTree.FindNodeByKey(75)
        self.assertIs(search_result.NodeHasKey, True)
        self.assertEqual(search_result.Node.NodeKey, 75)

        search_result = self.BinaryTree.FindNodeByKey(500)
        self.assertIs(search_result.NodeHasKey, False)
        self.assertEqual(search_result.Node.NodeKey, 400)
        self.assertIs(search_result.ToLeft, False)


    def test_find_min_max(self):
        self.BinaryTree.AddKeyValue(50, "value 50")
        self.BinaryTree.AddKeyValue(200, "value 200")
        self.BinaryTree.AddKeyValue(150, "value 150")
        self.BinaryTree.AddKeyValue(300, "value 300")

        self.assertIs(self.BinaryTree.FinMinMax(self.Root, False).NodeKey, 50)
        self.assertIs(self.BinaryTree.FinMinMax(self.Root.RightChild, False).NodeKey, 150 )
        self.assertIs(self.BinaryTree.FinMinMax(self.Root, True).NodeKey, 300)
        self.assertIs(self.BinaryTree.FinMinMax(self.Root.RightChild, True).NodeKey, 300)


    def test_delete_nodes(self):

        self.BinaryTree.AddKeyValue(50, "value 50")
        self.BinaryTree.AddKeyValue(200, "value 200")
        self.BinaryTree.AddKeyValue(150, "value 150")
        self.BinaryTree.AddKeyValue(300, "value 300")

        self.BinaryTree.DeleteNodeByKey(200)
        self.assertEqual(self.Root.RightChild.NodeKey, 300)
        self.assertIs(self.Root.RightChild.RightChild, None)
        self.assertIs(self.Root.RightChild.LeftChild.NodeKey, 150)
        self.assertEqual(self.Root.NodeKey, 100)


        self.BinaryTree.DeleteNodeByKey(100)
        self.assertEqual(self.BinaryTree.Root.NodeKey, 150)
        self.assertEqual(self.BinaryTree.Root.RightChild.NodeKey, 300)
        self.assertEqual(self.BinaryTree.Root.LeftChild.NodeKey, 50)
        self.assertIs(self.BinaryTree.Root.RightChild.RightChild, None)


        self.BinaryTree.DeleteNodeByKey(100)
        self.assertEqual(self.BinaryTree.Root.NodeKey, 150)
        self.assertEqual(self.BinaryTree.Root.RightChild.NodeKey, 300)
        self.assertEqual(self.BinaryTree.Root.LeftChild.NodeKey, 50)
        self.assertIs(self.BinaryTree.Root.RightChild.RightChild, None)
        self.assertIs(self.BinaryTree.Root.RightChild.LeftChild, None)


    def test_count(self):

        self.BinaryTree.AddKeyValue(50, "value 50")
        self.BinaryTree.AddKeyValue(200, "value 200")
        self.BinaryTree.AddKeyValue(150, "value 150")
        self.BinaryTree.AddKeyValue(300, "value 300")
        self.assertEqual(self.BinaryTree.Count(), 5)



if __name__ == "__main__":
    unittest.main()
