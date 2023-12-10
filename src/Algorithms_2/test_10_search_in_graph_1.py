import unittest
from problemset_10_search_in_graph_1 import SimpleGraph


class SimpleGraph_test(unittest.TestCase):


    def test_find_rout_in_graph(self):

        graph = SimpleGraph(5)
        for i in range(5):
            graph.AddVertex(i)

        for i in range(3):
            graph.AddEdge(i, i + 1)


        self.assertEqual(graph.DepthFirstSearch(0, 3), [graph.vertex[0], graph.vertex[1], graph.vertex[2], graph.vertex[3]])
        self.assertEqual(graph.DepthFirstSearch(1, 3), [graph.vertex[1], graph.vertex[2], graph.vertex[3]])
        self.assertEqual(graph.DepthFirstSearch(0, 4), [])


if __name__ == "__main__":
    unittest.main()
