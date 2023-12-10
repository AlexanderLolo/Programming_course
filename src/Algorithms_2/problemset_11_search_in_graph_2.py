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

    def build_array_from_stack(self):
        array = []
        tail_value = self.pop()
        while tail_value is not None:
            array.append(tail_value)
            tail_value = self.pop()
        return array

    def shallow_copy_stack(self):

        copy_stack = Stack()

        node = self.stack.head
        while node is not None:
            copy_stack.stack.add_in_tail(node)
            node = node.next
        return copy_stack

    def delete_stack(self):
        for _ in range(self.size()):
            self.pop()
        self.stack = None


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

    def BreadthFirstSearch(self, VFrom, VTo):

        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

        queue_all_routes = Queue()
        route = Stack()

        for vertex in self.vertex:
            vertex.Hit = False

        if VFrom == VTo:
            return [self.vertex[VFrom]]

        self.vertex[VFrom].Hit = True
        route.push(VFrom)
        queue_all_routes.enqueue(route)
        return self.check_next_layer_vertexes(queue_all_routes, VTo)

        # while queue_all_routes.size() > 0:

        #     current_rout = queue_all_routes.dequeue()
        #     current_vertex = current_rout.peek()

        #     adj_not_hit_vertexes = self.find_adjacent_not_hit_vertex(current_vertex)

        #     if len(adj_not_hit_vertexes) == 0:
        #         continue

        #     if VTo in adj_not_hit_vertexes:
        #         current_rout.push(VTo)
        #         indexes_of_rout_elems = current_rout.build_array_from_stack()[::-1]
        #         return [self.vertex[index] for index in indexes_of_rout_elems]

        #     self.add_adjacent_vertexes(queue_all_routes, current_rout, current_vertex)
        #     current_rout.delete_stack()
        # return []

    def check_next_layer_vertexes(self, queue_all_routes, VTo):

        if queue_all_routes.size() == 0:
            return []

        current_rout = queue_all_routes.dequeue()
        current_vertex = current_rout.peek()

        adj_not_hit_vertexes = self.find_adjacent_not_hit_vertex(current_vertex)

        if len(adj_not_hit_vertexes) == 0:
            return self.check_next_layer_vertexes(queue_all_routes, VTo)

        if VTo in adj_not_hit_vertexes:
            current_rout.push(VTo)
            indexes_of_rout_elems = current_rout.build_array_from_stack()[::-1]
            return [self.vertex[index] for index in indexes_of_rout_elems]

        self.add_adjacent_vertexes(queue_all_routes, current_rout, current_vertex)
        current_rout.delete_stack()
        return self.check_next_layer_vertexes(queue_all_routes, VTo)


    def add_adjacent_vertexes(self, queue_all_routes, route, vertex_from):

        for candidate_index, candidate_vertex  in enumerate(self.vertex):
            if (candidate_vertex is not None
                    and self.m_adjacency[vertex_from][candidate_index] == 1
                    and not candidate_vertex.Hit):
                self.vertex[candidate_index].Hit = True
                new_route = route.shallow_copy_stack()
                new_route.push(candidate_index)
                queue_all_routes.enqueue(new_route)


    def find_adjacent_not_hit_vertex(self, vertex_position):

        adjacent_vertexes = []

        for candidate_index, candidate_vertex  in enumerate(self.vertex):
            if (candidate_vertex is not None
                and self.m_adjacency[vertex_position][candidate_index] == 1
                and not candidate_vertex.Hit):
                adjacent_vertexes.append(candidate_index)
        return adjacent_vertexes
