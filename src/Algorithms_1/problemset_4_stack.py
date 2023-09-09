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

    def delete_from_tail(self):
        if self.tail is not self.head:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
            self.head = None

    def delete_from_head(self):
        if self.tail is not self.head:
            self.head = self.head.next
            self.head.prev = None
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


# class EmptyStackException(Exception):
#     pass


class Stack_old:

    def __init__(self):
        self.stack = LinkedList()

    def push(self, item):
        # O(1) complexity
        node = Node(item)
        self.stack.add_in_tail(node)

    def pop(self):
        # O(1) complexity
        # if self.stack.tail is None:
        #     raise EmptyStackException('''Stack is empty.Cant produce 'pop' ''')
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

        # if self.stack.tail is None:
        #     raise EmptyStackException('Stack is empty.Cant produce pop')
        # return self.stack.tail.value

    def size(self):
        return self.stack.get_size()

# The output of the following commands depends on the number of elements in stack.
# If the number is odd then all elements and "None" will be returned.
# while stack.size() > 0:
#     print(stack.pop())
#     print(stack.pop())


class Stack:

    def __init__(self):
        self.stack = LinkedList()

    def push(self, item):
        # O(1) complexity
        node = Node(item)
        self.stack.add_in_head(node)

    def pop(self):
        # O(1) complexity
        if self.stack.head is None:
            return None

        value = self.stack.head.value
        self.stack.delete_from_head()
        return value

    def peek(self):
        # O(1) complexity
        if self.stack.head is None:
            return None
        return self.stack.head.value

    def size(self):
        return self.stack.get_size()


def balance_parenthesis(string1: str) -> bool:
    stack = Stack()
    for element in string1:
        if element == "(":
            stack.push(1)
        else:
            a = stack.pop()
            if a is None:
                return False
    return stack.size() == 0


def postfix(string1: str) -> float:
    stack_num = Stack()
    # stack_oper = Stack()

    for element in string1.split(" "):
        if element == "=":
            return stack_num.pop()
        if element.isdigit():
            stack_num.push(int(element))
        if element == "+":
            stack_num.push(stack_num.pop() + stack_num.pop())
        if element == "*":
            stack_num.push(stack_num.pop() * stack_num.pop())
    return "incorrect string"
