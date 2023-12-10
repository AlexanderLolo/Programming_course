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

class Stack:

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

    def build_array_from_stack(self):
        array = []
        tail_value = self.pop()
        while tail_value is not None:
            array.append(tail_value)
            tail_value = self.pop()
        return array


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, node_value):
        if None not in self.vertex:
            return False
        free_slot = self.vertex.index(None)
        self.vertex[free_slot] = Vertex(node_value)
        return True

    def RemoveVertex(self, node_index):
        self.vertex[node_index] = None
        self.delete_all_adjacencies(node_index)

    def delete_all_adjacencies(self, node_index):
        for i in range(self.max_vertex):
            self.m_adjacency[i][node_index] = 0
            self.m_adjacency[node_index][i] = 0

    def IsEdge(self, from_node_index, to_node_index):
        return self.m_adjacency[from_node_index][to_node_index] == 1

    def AddEdge(self, from_node_index, to_node_index):
        self.m_adjacency[from_node_index][to_node_index] = 1
        self.m_adjacency[to_node_index][from_node_index] = 1

    def RemoveEdge(self, from_node_index, to_node_index):
        self.m_adjacency[from_node_index][to_node_index] = 0
        self.m_adjacency[to_node_index][from_node_index] = 0

    def DepthFirstSearch(self, VFrom, VTo):

        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

        stack = Stack()
        for vertex in self.vertex:
            vertex.Hit = False

        return self.find_route_in_graph(VFrom, VTo, stack)

    def find_route_in_graph(self, vertex_from, vertex_to, stack):

        self.vertex[vertex_from].Hit = True
        stack.push(vertex_from)

        if self.m_adjacency[vertex_from][vertex_to] == 1:
            stack.push(vertex_to)
            indexes_of_rout_elems = stack.build_array_from_stack()[::-1]
            return [self.vertex[index] for index in indexes_of_rout_elems]

        for _ in range(stack.size()):
            adjacent_vertex_index = self.find_adjacent_not_hitted_vertex(vertex_from)
            if adjacent_vertex_index is None:
                stack.pop()
                vertex_from = stack.peek()
                continue
            break

        if stack.size() == 0:
            return []
        return self.find_route_in_graph(adjacent_vertex_index, vertex_to, stack)


    def find_adjacent_not_hitted_vertex(self, vertex_position):

        for candidate_index, candidate_vertex  in enumerate(self.vertex):
            if (candidate_vertex is not None
                and self.m_adjacency[vertex_position][candidate_index] == 1
                and candidate_vertex.Hit is False):
                return candidate_index
        return None
