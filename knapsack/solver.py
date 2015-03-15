#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def prep_output(value,taken,items):
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    print "Taken value:",taken
    takenString = ""
    for i in xrange(0,len(items)):
        if taken & 1 == 1:
	    takenString += ' 1'
        else:
            takenString += ' 0'
        taken /= 2
    output_data += takenString[::-1]
    return output_data

# returns maximum value 
# params, capacity - space available
# items, list of items sorted by value/weight
def max_possible(capacity, items):
    value = 0
    weight = 0
    taken = 0

    print "Items: ",str(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken += 2 ** item.index
            value += item.value
            weight += item.weight
    return value, weight, taken 
    
def quick_solution(capacity,items):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = 0

    takenIndicator = 1
    for item in items:
        if weight + item.weight <= capacity:
            taken += takenIndicator
            value += item.value
            weight += item.weight
        takenIndicator *= 2
    return( value, weight, taken )
    
def rec_solution(capacity,items):
    value, weight, taken = 0,0,0
    if ( len(items) > 0 ):
        withoutTuple = rec_solution(capacity,items[1:])
        withoutTuple = (withoutTuple[0], withoutTuple[1], withoutTuple[2]*2)
	if (items[0].weight <= capacity ):
	    withTuple = rec_solution(capacity-items[0].weight, items[1:])
            withTuple = (withTuple[0]+items[0].value,withTuple[1]+items[0].weight,1+2*withTuple[2])
        else:
	    return withoutTuple
        if ( withTuple[0] > withoutTuple[0] ):
            return withTuple
        else:
            return withoutTuple
    return( value, weight, taken )

def subset_items( items, maskToRemove ):
    bitmask = 1
    itemIdx = 0
    itemAdj = 0
    return_items = []
    print "subset_items items: ",str(items)
    while ( itemIdx < len(items)):
        if ( False == (bitmask & maskToRemove) ):
	       return_items.append(items[itemIdx])
        bitmask *= 2
        itemIdx += 1
    print "return_items: ",str(return_items)
    return return_items

# pass in the best value, weight, taken set we have
# initially we'll remove one item and see if we can improve capacity
def improve_solution( value, weight, taken, capacity, items ):
    # Remove more and more items from the solution to see if we can improve results
    bitMask = 1
    itemsToRemove = 1
    best_solution = ( Item(value, weight, taken ) )
    # iteratively, remove one selected item, and attempt to improve results
    # we want to go through one level deep for each initially, 
    itemIdx = 0
    print "Items: ",str(len(items))
    print "Taken: ",str(taken)
    while ( bitMask <= taken ):
        if ( bitMask & taken ):
           itemsToTry = subset_items( items, bitMask )
	   print "subset_items; ",str(itemsToTry)
	   print "ItemIdx: ",str(itemIdx),str(bitMask)
	   result = max_possible( capacity + items[itemIdx].weight, itemsToTry )
	   print "MaxPossible result: ",str(result)
           if ( result[0] > best_solution[0] ):
               best_solution = result
               print "Improved Solution"
	       print prep_output( best_solution[0], best_solution[2], items) 
	bitMask *= 2
	itemIdx += 1
    return best_solution

def solve_it(capacity, items):
    # Modify this code to run your optimization algorithm

    value, weight, taken = quick_solution(capacity,items)

    value, weight, taken = improve_solution( value, weight, taken, capacity, items )

    print "Capacity: ",capacity
    recTuple =rec_solution(capacity,items )
    rec_results =prep_output(recTuple[0], recTuple[2],items ) 
    print "Recursive Solution: ",str(rec_results)

    for item in items:
        print str(item),str(float(item.value)/item.weight)

    output_data = prep_output(value,taken,items)

    return output_data

def prepData(file_location):
    input_data_file = open(file_location, 'r')
    input_data = ''.join(input_data_file.readlines())
    input_data_file.close()
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    items = sorted(items,key=lambda item:(-float(item.value)/item.weight))
    return (capacity, items)


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
	capacity, items = prepData(file_location)
        print solve_it(capacity, items)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

