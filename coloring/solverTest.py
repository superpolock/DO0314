import solver
import unittest

class Samples(unittest.TestCase):
    simple = "4 3\n0 1\n1 2\n1 3"

    def testParseIt(self):
        node_count, edge_count, edges, line, parts = solver.parse_it(self.simple)
        self.assertTrue(node_count,4)
        self.assertTrue(edge_count,3)
        self.assertTrue(edges[0],(0,1))
        self.assertTrue(edges[1],(1,2))
        self.assertTrue(edges[2],(1,3))

if __name__ == "__main__":
        unittest.main()   
