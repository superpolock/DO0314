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

	def test_bestFillYet(self):
		taken = [0]*len(self._items)
		print solver.fill_it(self._capacity, self._items, taken )
		self.assertLessEqual(7,solver.fill_it(self._capacity, self._items, taken )[0])
		self.assertGreaterEqual(solver.fill_it(self._capacity, self._items, taken )[0],35)

if __name__ == '__main__':
    unittest.main()	