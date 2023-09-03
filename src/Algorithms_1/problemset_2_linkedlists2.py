class Node:

    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList2:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.next = None
            item. prev = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return

    def find_all(self, val):
        listnode = []
        node = self.head
        while node is not None:
            if node.value == val:
                listnode.append(node)
            node = node.next
        return listnode

    def delete(self, val, fall=False):

        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None and node.next is None:
                    self.head = None
                    self.tail = None
                    return None

                if node.prev is None:
                    self.head = node.next
                    self.head.prev = None
                    node.next = None
                    if not fall:
                        return None
                    node = self.head
                    continue

                if node.next is None:
                    self.tail = node.prev
                    self.tail.next = None
                    node.prev = None
                    return None

                node.prev.next = node.next
                node.next.prev = node.prev
                if not fall:
                    return None
            node = node.next
        return None

    def clean(self):
        node = self.head
        while node is not None:
            self.head = node.next
            if node.next is not None:
                node.next.prev = None
                node.next = None
            node = self.head
        self.tail = None

    def len(self):
        leng = 0
        node = self.head
        while node is not None:
            leng += 1
            node = node.next
        return leng

    def insert(self, afterNode, newNode):

        if afterNode is None:
            self.add_in_tail(newNode)
            return None
        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next = newNode

        if newNode.next is not None:
            newNode.next.prev = newNode
        else:
            self.tail = newNode
        return None

    def add_in_head(self, newNode):

        newNode.next = self.head
        newNode.prev = None
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
        if self.tail is None:
            self.tail = newNode
