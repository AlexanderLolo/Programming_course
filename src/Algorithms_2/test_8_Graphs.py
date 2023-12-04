import unittest
from problemset_8_Graphs import SimpleGraph


class Graph_test(unittest.TestCase):


    def test_all_functions(self):
        test_graph = SimpleGraph(3)
        self.assertIs(test_graph.AddVertex(0), True)
        for i in range(3):
            self.assertIs(test_graph.IsEdge(0,i), False)

        self.assertIs(test_graph.AddVertex(1), True)
        for i in range(3):
            self.assertIs(test_graph.IsEdge(1,i), False)


        self.assertIs(test_graph.AddVertex(2), True)
        for i in range(3):
            self.assertIs(test_graph.IsEdge(2,i), False)

        self.assertIs(test_graph.AddVertex(3), False)


        test_graph.AddEdge(0, 1)
        self.assertIs(test_graph.IsEdge(0,1), True)
        self.assertIs(test_graph.IsEdge(1,0), True)

        test_graph.RemoveEdge(1, 0)
        self.assertIs(test_graph.IsEdge(0,1), False)
        self.assertIs(test_graph.IsEdge(1,0), False)

        test_graph.AddEdge(0, 1)
        test_graph.AddEdge(1, 2)
        test_graph.AddEdge(2, 0)
        test_graph.RemoveVertex(0)
        self.assertIs(test_graph.vertex[0], None)
        self.assertIs(test_graph.IsEdge(0,1), False)
        self.assertIs(test_graph.IsEdge(1,0), False)
        self.assertIs(test_graph.IsEdge(0,2), False)
        self.assertIs(test_graph.IsEdge(2,0), False)



if __name__ == "__main__":
    unittest.main()
