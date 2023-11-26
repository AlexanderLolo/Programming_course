class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок

class BSTFind: # промежуточный результат поиска
    def __init__(self):
        self.Node = None # None если в дереве вообще нету узлов
        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def construct_bstfind_result(self, node: BSTNode, is_node_has_key: bool, is_to_left: bool) -> BSTFind:
        search_result = BSTFind()
        search_result.Node = node
        search_result.NodeHasKey = is_node_has_key
        search_result.ToLeft = is_to_left
        return search_result

    def should_search_right_child(self, key: int, bst_node: BSTNode) -> bool:
        return key > bst_node.NodeKey and bst_node.RightChild is not None

    def should_search_left_child(self, key: int, bst_node: BSTNode) -> bool:
        return key < bst_node.NodeKey and bst_node.LeftChild is not None

    def can_be_right_child(self, key: int, bst_node: BSTNode) -> bool:
        return key > bst_node.NodeKey and bst_node.RightChild is None

    def can_be_left_child(self, key: int, bst_node: BSTNode) -> bool:
        return key < bst_node.NodeKey and bst_node.LeftChild is None


    def CheckNodesWithKey(self, key: int, bst_node: BSTNode) -> BSTFind:
        # ищем в дереве узел и сопутствующую информацию по ключу
        if self.should_search_right_child(key, bst_node):
            return self.CheckNodesWithKey(key, bst_node.RightChild)

        if self.should_search_left_child(key, bst_node):
            return self.CheckNodesWithKey(key, bst_node.LeftChild)

        if self.can_be_left_child(key, bst_node):
            return self.construct_bstfind_result(bst_node, False, True)

        if self.can_be_right_child(key, bst_node):
            return self.construct_bstfind_result(bst_node, False, False)

        if bst_node.NodeKey == key:
            return self.construct_bstfind_result(bst_node, True, False)

    def FindNodeByKey(self, key: int) -> BSTFind:
        if self.Root is None:
            return BSTFind()
        return self.CheckNodesWithKey(key, self.Root)


    def AddKeyValue(self, key: int, val: str) -> bool:
        # функция добавляет ключ-значение в дерево
        search_node_by_key_result = self.FindNodeByKey(key)
        if search_node_by_key_result.Node is None: # если в дереве нет узлов
            self.Root = BSTNode(key, val, None)
            return True

        if search_node_by_key_result.NodeHasKey is True:
            return False # если ключ уже есть

        if search_node_by_key_result.ToLeft is True:
            new_node = BSTNode(key, val, search_node_by_key_result.Node)
            search_node_by_key_result.Node.LeftChild = new_node
            return True

        if search_node_by_key_result.ToLeft is False:
            new_node = BSTNode(key, val, search_node_by_key_result.Node)
            search_node_by_key_result.Node.RightChild = new_node
            return True

    def FinMinMax(self, fromNode: BSTNode, findMax: bool) -> BSTNode:
        # ищет максимальный/минимальный ключ в поддереве и возвращается объект типа BSTNode
        if fromNode is None:
            return None
        if findMax:
            return self.FindMax(fromNode)
        return self.FindMin(fromNode)

    def FindMin(self, FromNode: BSTNode) -> BSTNode:
        node = FromNode
        while node.LeftChild is not None:
            node = node.LeftChild
        return node

    def FindMax(self, FromNode: BSTNode) -> BSTNode:
        node = FromNode
        while node.RightChild is not None:
            node = node.RightChild
        return node

    def DeleteNodeByKey(self, key: int) -> bool:
        # функция удаляет узел по ключу
        search_by_key_result = self.FindNodeByKey(key)

        # если узел не найден
        if search_by_key_result.NodeHasKey is False:
            return False

        # если нет вообще потомков
        if self.is_leaf(search_by_key_result.Node):
            self.delete_leaf(search_by_key_result.Node)
            return True

        REPLACE_WITHOUT_BRANCHES = True

        # если нет правого потока
        if search_by_key_result.Node.RightChild is None:
            self.replace_nodes(search_by_key_result.Node,
                               search_by_key_result.Node.LeftChild, not REPLACE_WITHOUT_BRANCHES)
            return True

        # если у правого потомка нет левого потомка
        if search_by_key_result.Node.RightChild.LeftChild is None:
            # перенаправляем левого потомка удаляемого узла, левым потомком к правому потомку
            search_by_key_result.Node.LeftChild.Parent = search_by_key_result.Node.RightChild
            search_by_key_result.Node.RightChild.LeftChild = search_by_key_result.Node.LeftChild
            search_by_key_result.Node.LeftChild = None

            self.replace_nodes(search_by_key_result.Node,
                               search_by_key_result.Node.RightChild, not REPLACE_WITHOUT_BRANCHES)
            return True

        # если у правого потомка есть левый потомок, то ищем минимальный ключ
        node_with_min_key = self.FindMin(search_by_key_result.Node.RightChild)

        if self.is_leaf(node_with_min_key):
            node_with_min_key.Parent.LeftChild = None
            self.replace_nodes(search_by_key_result.Node,
                               node_with_min_key, REPLACE_WITHOUT_BRANCHES)

        else:
            self.replace_nodes(node_with_min_key,
                               node_with_min_key.RightChild,
                               not REPLACE_WITHOUT_BRANCHES)
            self.replace_nodes(search_by_key_result.Node,
                               node_with_min_key,
                               REPLACE_WITHOUT_BRANCHES)
        return True

    def delete_leaf(self, node_to_delete: BSTNode) -> None:
        if node_to_delete is self.Root:
            self.Root = None
            return None

        if node_to_delete.Parent.LeftChild is node_to_delete:
            node_to_delete.Parent.LeftChild = None
        else:
            node_to_delete.Parent.RightChild = None

        node_to_delete.Parent = None
        return None


    def replace_nodes(self, node_to_substitute: BSTNode, node_to_insert: BSTNode, is_without_branches: bool) -> None:
        # если is_without_branches is True, то оставляем ветви узла, который мы заменили
        if node_to_substitute is self.Root:
            node_to_insert.Parent = None
            self.Root = node_to_insert

        elif node_to_substitute.Parent.LeftChild is node_to_substitute:
            node_to_substitute.Parent.LeftChild = node_to_insert
            node_to_insert.Parent = node_to_substitute.Parent

        else:
            node_to_substitute.Parent.RightChild = node_to_insert
            node_to_insert.Parent = node_to_substitute.Parent

        if is_without_branches:
            node_to_insert.RightChild = node_to_substitute.RightChild
            node_to_insert.LeftChild = node_to_substitute.LeftChild

        node_to_substitute.RightChild = None
        node_to_substitute.LeftChild = None
        node_to_substitute.Parent = None

    def is_leaf(self, node: BSTNode) -> bool:
        return node.LeftChild is None and node.RightChild is None

    def Count(self) -> int:
		# подсчитываем количество узлов
        if self.Root is None:
            return 0
        return self.Num_Of_Nodes(self.Root)

    def Num_Of_Nodes(self, node: BSTNode) -> int:
        num_of_nodes = 1

        if node.LeftChild is not None:
            num_of_nodes += self.Num_Of_Nodes(node.LeftChild)
        if node.RightChild is not None:
            num_of_nodes += self.Num_Of_Nodes(node.RightChild)

        return num_of_nodes
