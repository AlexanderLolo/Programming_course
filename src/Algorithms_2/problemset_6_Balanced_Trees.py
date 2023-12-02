class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None # корень дерева

    def GenerateTree(self, list_of_nodes):
    # создаём дерево с нуля из неотсортированного массива a
        sorted_array_of_nodes = sorted(list_of_nodes)
        if len(list_of_nodes) == 0:
            return None

        self.Root = self.insert_node(None, sorted_array_of_nodes, 0, len(sorted_array_of_nodes))
        self.Root.Level = 0

    def insert_node(self, parent, sorted_array_of_nodes, first_elem_index, last_elem_index):
    # first_elem_index, last_elem_index - границы диапазона из которого выбираем средний элемент

        if first_elem_index == last_elem_index:
            return None
        central_element = (last_elem_index + first_elem_index) // 2
        node = BSTNode(sorted_array_of_nodes[central_element], parent)
        if node.Parent is not None:
            node.Level = node.Parent.Level + 1

        node.LeftChild = self.insert_node(node, sorted_array_of_nodes,
                                          first_elem_index, central_element)
        node.RightChild = self.insert_node(node, sorted_array_of_nodes,
                                           central_element + 1, last_elem_index)

        return node


    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        is_left_child_balanced = True
        left_child_depth = root_node.Level
        if root_node.LeftChild is not None:
            is_left_child_balanced = self.IsBalanced(root_node.LeftChild)
            left_child_depth = self.get_tree_depth(root_node.LeftChild)

        is_right_child_balanced = True
        right_child_depth = root_node.Level
        if root_node.RightChild is not None:
            is_right_child_balanced = self.IsBalanced(root_node.RightChild)
            right_child_depth = self.get_tree_depth(root_node.RightChild)

        return (is_right_child_balanced
                and is_left_child_balanced
                and abs(left_child_depth - right_child_depth) <= 1)


    def get_tree_depth(self, root_node):
        if root_node.LeftChild is None and root_node.RightChild is None:
            return root_node.Level
        if root_node.LeftChild is not None and root_node.RightChild is None:
            return self.get_tree_depth(root_node.LeftChild)
        if root_node.LeftChild is None and root_node.RightChild is not None:
            return self.get_tree_depth(root_node.RightChild)

        return max(self.get_tree_depth(root_node.RightChild),
                   self.get_tree_depth(root_node.LeftChild))

    def IsCorrect(self, root_node):
        if root_node is None:
            return True
        if (root_node.LeftChild is not None and root_node.LeftChild.NodeKey > root_node.NodeKey
            or root_node.RightChild is not None and root_node.RightChild.NodeKey < root_node.NodeKey):
            return False
        return self.IsCorrect(root_node.LeftChild) and self.IsCorrect(root_node.RightChild)
