class Vertex:

    def __init__(self, val):
        self.Value = val

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
