import unittest
from problemset_11_search_in_graph_2 import SimpleGraph


class SimpleGraph_test(unittest.TestCase):


    def test_find_rout_in_graph(self):

        graph = SimpleGraph(5)
        for i in range(5):
            graph.AddVertex(i)

        for i in range(4):
            graph.AddEdge(i, i + 1)
        graph.AddEdge(0, 4)


        self.assertEqual(graph.BreadthFirstSearch(0, 4), [graph.vertex[0], graph.vertex[4]])
        self.assertEqual(graph.BreadthFirstSearch(1, 3), [graph.vertex[1], graph.vertex[2], graph.vertex[3]])
        self.assertEqual(graph.BreadthFirstSearch(1, 4), [graph.vertex[1], graph.vertex[0], graph.vertex[4]])


if __name__ == "__main__":
    unittest.main()
