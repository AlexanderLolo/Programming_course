## class names
# 1

    class LinkedList:   ##### class SingleLinkedList (первое и второе слова не являются существительным, но имена вроде смотрятся нормально)
    class LinkedList2:  ##### class DoubleLinkedList

# 2

    class MoolokSP(Spaceship) ##### MoolokSpaceship(Spaceship)
    class HumanSP(Spaceship) ##### HumanSpaceship(Spaceship)

# 3

    class Human(Ranger):##### HumanRanger(Ranger)
    class Moolok(Ranger): ##### MoolokRanger(Ranger)

# 4
    class Stack ##### TailStack
    class Stack_old #### HeadStack

# 5

    class OrderedStringList ##### StringOrderedList


## methods names

# 1

    class DynArray:
        def __getitem__(self, pos):

    class LinkedList2:
        def find(self, val): ##### def __getitem__(self, val): # интересно, не вводит ли это имя в заблуждение, так как мы ищем узел, а не элемент

# 2

    class LinkedList2:
        def len(self): ##### def get_size(self)

    class LinkedList:
        def get_size(self):

    class Stack_old:
        def size(self): ##### def get_size(self)

    class Queue:
        def size(self): ##### def get_size(self)


# 3

    class Queue:
        def enqueue(self, item): ##### def add_in_tail(self, item):

    class LinkedList:
        def add_in_tail(self, item): ##### а вообще, наверное лчше назвать метод append

# 4

    class LinkedList:
        def delete_from_head(self):

    class Queue:
        def dequeue(self): ##### def delete_from_head(self):

# 5

    class LinkedList:
        def add_in_tail(self, item):

    class Deque:
        def addTail(self, item): ##### def add_in_tail(self, item):

# 6

    list1 = LinkedList() ##### first_linkedlist =...
    list2 = LinkedList() ##### second_linkedlist =...

    a = Node(128) ##### first_node = ...
    b = Node(11)  ##### second_node = ...

# 7

    s_list = OrderedList(True)  ##### asc_ordered_list = ...
    s_list = OrderedList(False) ##### des_ordered_list = ...

