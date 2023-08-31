class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        listnode = []
        node = self.head
        while node is not None:
            if node.value == val:
                listnode.append(node)
            node = node.next
        return listnode

    def delete(self, val, all=False):
        node = self.head
        if self.head is None:
            return None

        while node.value == val:
            self.head = node.next
            if node.next is None:
                self.tail = None
                return None
            if not all:
                return None
            node = node.next

        while node.next is not None:
            if node.next.value == val and node.next.next is None:
                node.next = None
                self.tail = node
                return None
            if node.next.value == val:
                node.next = node.next.next
                if not all:
                    return None
            if node.next.value != val:
                node = node.next
        return None

    def clean(self):
        node = self.head
        while node is not None:
            self.head = node.next
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
        afterNode.next = newNode
        if newNode.next is None:
            self.tail = newNode
        return None
