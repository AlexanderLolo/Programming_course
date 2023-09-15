class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:

    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
        return 0

    def add(self, item):

        node = self.head
        while node is not None:
            if (self.__ascending and self.compare(item, node.value) == 1 or
                    not self.__ascending and self.compare(item, node.value) == -1):
                node = node.next
                continue
            break

        newNode = Node(item)

        if node is None:
            newNode.prev = self.tail
            newNode.next = None
            if node is self.head:
                self.head = newNode
            else:
                self.tail.next = newNode
            self.tail = newNode
            return None

        newNode.next = node
        newNode.prev = node.prev
        if node is self.head:
            self.head = newNode
        else:
            node.prev.next = newNode
        node.prev = newNode
        return None

    def delete(self, val, fall=False):

        node = self.head
        while node is not None:
            if (self.compare(node.value, val) == 1 and self.__ascending or
                    self.compare(node.value, val) == -1 and not self.__ascending):
                return None

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

    def find(self, val):
        node = self.head
        while node is not None:
            if (self.compare(node.value, val) == 1 and self.__ascending or
                    self.compare(node.value, val) == -1 and not self.__ascending):
                return None

            if node.value == val:
                return node
            node = node.next
        return None

    def clean(self, asc):
        self.__ascending = asc
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
    
    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() > v2.strip():
            return 1
        if v1.strip() < v2.strip():
            return -1
        return 0
