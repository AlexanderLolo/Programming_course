class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

class SimpleTree:

    def __init__(self,root):
        self.Root = root # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            self.Root = NewChild
        else:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
		# удаление некорневого узла
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        for children_node in NodeToDelete.Children:
            self.DeleteNode(children_node)

    def GetAllNodes(self):
        if self.Root is None:
            return []
        all_children_nodes = self.GetAllChildrenNodes(self.Root)
        all_children_nodes.append(self.Root)
        return all_children_nodes

    def GetAllChildrenNodes(self, parent_node):
        all_children_nodes = []

        for children_node in parent_node.Children:
            all_children_nodes.append(children_node)
            next_layer_children_nodes = self.GetAllChildrenNodes(children_node)
            all_children_nodes.extend(next_layer_children_nodes)

        return all_children_nodes

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []
        nodes_with_target_val = self.FindChildNodesByValue(val, self.Root)
        if self.Root.NodeValue == val:
            nodes_with_target_val.append(self.Root)
        return nodes_with_target_val

    def FindChildNodesByValue(self, val, parent_node):
        nodes_with_target_val = []
        for children_node in parent_node.Children:
            if children_node.NodeValue == val:
                nodes_with_target_val.append(children_node)
            next_layer_nodes_with_target_val = self.FindChildNodesByValue(val, children_node)
            nodes_with_target_val.extend(next_layer_nodes_with_target_val)
        return nodes_with_target_val

    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
		# количество узлов
        if self.Root is None:
            return 0

        return self.Num_leaves_or_nodes(self.Root, False)

    def LeafCount(self):
		# количество листьев
        if self.Root is None or len(self.Root.Children) == 0:
            return 0

        return self.Num_leaves_or_nodes(self.Root, True)

    def Num_leaves_or_nodes(self, node, isLeaves):
        num_of_nodes = 0
        num_of_leaves = 0

        if len(node.Children) == 0:
            num_of_leaves += 1
        else:
            num_of_nodes += 1

        for children_node in node.Children:
            num_of_nodes += self.Num_leaves_or_nodes(children_node, False)
            num_of_leaves += self.Num_leaves_or_nodes(children_node, True)

        if isLeaves:
            return num_of_leaves
        return num_of_nodes
