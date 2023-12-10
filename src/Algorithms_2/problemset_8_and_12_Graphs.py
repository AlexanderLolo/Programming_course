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

    def WeakVertices(self):
        # возвращает список узлов вне треугольников
        weak_vertices = set()
        adj_matrix = {}

        for vertex_index in range(self.max_vertex):
            if self.vertex[vertex_index] is not None:
                adj_matrix[vertex_index] = self.find_adjacent_vertices(vertex_index)

        for vertex_index, adj_vertices in adj_matrix.items():
            if not self.is_any_adj_vertices_linked(adj_vertices, adj_matrix):
                weak_vertices.add(vertex_index)

        return [self.vertex[vertex_indx] for vertex_indx in weak_vertices]

    def is_any_adj_vertices_linked(self, adj_vertices, adj_matrix):

        for adj_vetrex in adj_vertices:
            common_adjacent = adj_matrix[adj_vetrex].intersection(adj_vertices)
            if  common_adjacent != set():
                return True
        return False


    def find_adjacent_vertices(self, vertex_position):

        adjacent_vertexes = set()

        for candidate_index, candidate_vertex  in enumerate(self.vertex):
            if (candidate_vertex is not None
                    and self.m_adjacency[vertex_position][candidate_index] == 1):
                adjacent_vertexes.add(candidate_index)
        return adjacent_vertexes
