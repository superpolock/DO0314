import unittest
import solver

class solverTest(unittest.TestCase):

	def setUp(self):
		test = solver.SolverFilePrep()
		fileLines = test.prepData("data/ks_lecture_dp_2")
		self._capacity, self._items = test.getData(fileLines)
		print "Capacity: " + str(self._capacity)
		print "Items: " + str(self._items)
		print "Finished setup"

	def test_confirmLines(self):
		print self._items
		self.assertLess(0,self._items)

	def test_basics(self):
		self.assertLess( self._capacity, solver.greatestPossible( self._capacity, self._items ) )

if __name__ == '__main__':
    unittest.main()	