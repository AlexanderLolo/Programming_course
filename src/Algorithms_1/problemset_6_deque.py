class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            self.head.prev = None
            self.head.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, item):
        if self.head is None:
            self.tail = item
            self.tail.prev = None
            self.tail.next = None
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item

    def delete_from_head(self):
        if self.tail is not self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.tail = None
            self.head = None

    def delete_from_tail(self):
        if self.tail is not self.head:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
            self.head = None

    def get_size(self):
        leng = 0
        node = self.head
        while node is not None:
            leng += 1
            node = node.next
        return leng

    def is_empty(self):
        return self.tail is None


class Deque:

    def __init__(self):
        self.queue = LinkedList()

    def addTail(self, item):
        # O(1) complexity
        node = Node(item)
        self.queue.add_in_tail(node)

    def addFront(self, item):
        # O(1) complexity
        node = Node(item)
        self.queue.add_in_head(node)

    def removeFront(self):
        # O(1) complexity
        if self.queue.head is None:
            return None

        value = self.queue.head.value
        self.queue.delete_from_head()
        return value
    
    def removeTail(self):
        # O(1) complexity
        if self.queue.tail is None:
            return None

        value = self.queue.tail.value
        self.queue.delete_from_tail()
        return value
    
    def size(self):
        return self.queue.get_size()
    
def palindrom(string1: str) -> bool:
    deque = Deque()
    for element in string1:
        deque.addTail(element)

    for _ in range(deque.size() // 2):
        if deque.removeTail() != deque.removeFront():
            return False
    return True
