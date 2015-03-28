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

    def testSolveIt(self):
        results = solver.solve_it(self.simple)
        lines = results.splitlines()
# and the second object was whether or not solution is optimal
        colors = set()
        nodeIdx = 0
        nodes = {}
        for color in lines[1].split():
            colors.add(int(color))
            nodes[nodeIdx]=color
            nodeIdx += 1
# first line is the number of colors
        self.assertEqual(lines[0],"4 0")
        print 'Nodes: ',str(nodes)
        self.assertEqual(len(colors),2)
        self.assertTrue(1 in colors)
        self.assertTrue(0 in colors)
        self.assertTrue(2 not in colors)
        self.assertTrue(3 not in colors)

    def testFindLowest(self):
        sampleList = [4,3,2,1]
        print min(sampleList)
        self.assertTrue(1 == min(sampleList))
if __name__ == "__main__":
        unittest.main()   
