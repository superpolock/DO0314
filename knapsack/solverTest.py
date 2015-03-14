import unittest
import solver

class solverTest(unittest.TestCase):

	def setUp(self):
		self._capacity, self._items = solver.prepData("data/ks_lecture_dp_2")
		print "Capacity: " + str(self._capacity)
		print "Items: " + str(self._items)
		print "Finished setup"

	def test_confirmLines(self):
		print self._items
		self.assertLess(0,self._items)

	def test_basics(self):
		self.assertLess( self._capacity, solver.max_possible( self._capacity, self._items )[0] )

	def test_bestFillYet(self):
		taken = 0
		results = solver.quick_solution(self._capacity,self._items)
		self.assertLessEqual(7,results[0])
		self.assertGreaterEqual(results[0],35)

	def test_ks_lecture_dp_1(self):
		capacity, items = solver.prepData("data/ks_lecture_dp_1")
		valueStuffed, weight, takenMap = solver.solve_it(capacity,items)
		self.assertEquals(valueStuffed,11)
	     
        def test_subset(self):
		items = [solver.Item(1,2,3)]
		items += solver.Item(3,4,5)
		print items
		result = solver.subset_items( items, 0 )
		self.assertEquals(result,items)

if __name__ == '__main__':
    unittest.main()	
