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


class Queue:

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        # O(1) complexity
        node = Node(item)
        self.queue.add_in_tail(node)

    def dequeue(self):
        # O(1) complexity
        if self.queue.head is None:
            return None

        value = self.queue.head.value
        self.queue.delete_from_head()
        return value

    def size(self):
        return self.queue.get_size()


class Stack:

    def __init__(self):
        self.stack = LinkedList()

    def push(self, item):
        # O(1) complexity
        node = Node(item)
        self.stack.add_in_tail(node)

    def pop(self):
        # O(1) complexity
        if self.stack.tail is None:
            return None

        value = self.stack.tail.value
        self.stack.delete_from_tail()
        return value

    def peek(self):
        # O(1) complexity
        if self.stack.tail is None:
            return None
        return self.stack.tail.value

    def size(self):
        return self.stack.get_size()

    def is_empty(self):
        return self.stack.is_empty()


class Two_stack_Queue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        # O(n) complexity
        from_stack_to_stack(self.stack1, self.stack2)
        self.stack1.push(item)

    def dequeue(self):
        # O(n) complexity
        from_stack_to_stack(self.stack2, self.stack1)
        return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()


def from_stack_to_stack(stack_1, stack_2):
    while not stack_2.is_empty():
        stack_1.push(stack_2.pop())


def rotate_queue(queue, N):
    if queue.size() == 0:
        return None
    for _ in range(N):
        queue.enqueue(queue.dequeue())
    return None


# task 1.8 from 1st lesson
def sum_if_len_equal(list1, list2):
    if list1.get_size() != list2.get_size():
        return None
    list3 = LinkedList()
    node1 = list1.head
    node2 = list2.head
    for _ in range(list1.get_size()):
        list3.add_in_tail(Node(node1.value + node2.value))
        node1 = node1.next
        node2 = node2.next
    return list3


# task 2.10 from 2nd lesson. Still struggling to make dummy head and tail inaccessible without implicitly or explicitly considering two cases:
# adding/deleting from 1) middle and from 2) end of the linkedlist
class LinkedList_with_dummy_nodes:

    def __init__(self):
        self.__head = Node(None)
        self.__tail = Node(None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        item.prev = self.__tail.prev
        item.next = self.__tail
        self.__tail.prev = item
        item.prev.next = item
        self.head = self.__head.next
        self.tail = self.__tail.prev

    def insert(self, afterNode, newNode):

        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode
            newNode.next.prev = newNode
        self.head = self.__head.next
        self.tail = self.__tail.prev

    def delete(self, val, fall=False):
        node = self.__head.next
        while node.next is not None:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not fall:
                    return None
            node = node.next

        if self.__head.next is self.__tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.__head.next
            self.tail = self.__tail.prev
        return None
