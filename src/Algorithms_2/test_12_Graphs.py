import unittest
from problemset_8_and_12_Graphs import SimpleGraph


class Graph_test(unittest.TestCase):


    def test_all_functions(self):
        test_graph = SimpleGraph(9)
        self.assertEqual(set(test_graph.WeakVertices()), set())
        for i in range(9):
            test_graph.AddVertex(i)

        self.assertEqual(set(test_graph.WeakVertices()), set(test_graph.vertex[i] for i in range(9)))

        test_graph.AddEdge(0, 1)
        test_graph.AddEdge(1, 2)
        test_graph.AddEdge(2, 3)
        test_graph.AddEdge(3, 1)
        test_graph.AddEdge(3, 4)
        test_graph.AddEdge(4, 5)
        test_graph.AddEdge(5, 6)
        test_graph.AddEdge(6, 7)
        test_graph.AddEdge(7, 8)
        test_graph.AddEdge(3, 8)
        test_graph.AddEdge(5, 8)
        test_graph.AddEdge(6, 8)

        self.assertEqual(set(test_graph.WeakVertices()), {test_graph.vertex[0], test_graph.vertex[4]})



if __name__ == "__main__":
    unittest.main()
