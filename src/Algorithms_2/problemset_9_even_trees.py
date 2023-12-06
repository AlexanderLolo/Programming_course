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
		# подсчитываем количество узлов
        if self.Root is None:
            return 0
        return self.Num_Of_Nodes(self.Root)

    def Num_Of_Nodes(self, node):
        num_of_nodes = 1

        for children_node in node.Children:
            num_of_nodes += self.Num_Of_Nodes(children_node)
        return num_of_nodes

    def LeafCount(self):
		# подсчитываем количество листьев
        if self.Root is None:
            return 0

        return self.Num_Of_Leaves(self.Root)

    def Num_Of_Leaves(self, node):
        num_of_leaves = 0
        if len(node.Children) == 0:
            num_of_leaves += 1

        for children_node in node.Children:
            num_of_leaves += self.Num_Of_Leaves(children_node)

        return num_of_leaves

    def EvenTrees(self):
        list_of_all_nodes = self.GetAllNodes()

        list_of_nodes_with_deleted_connection = []

        for node in list_of_all_nodes:
            if self.Num_Of_Nodes(node) % 2 == 0 and node.Parent is not None:
                list_of_nodes_with_deleted_connection.append(node.Parent) 
                list_of_nodes_with_deleted_connection.append(node)
        return list_of_nodes_with_deleted_connection
