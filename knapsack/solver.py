#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def format_data( lines ):
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    return capacity, items

# Taken will be an integer which represents all bits which are in use
def is_taken( taken, itemIdx ):
    return ( taken & ( 1 << itemIdx ) ) != 0

# isSet is true if we are setting value and false if we are clearing it
def set_taken( taken, itemIdx, setBit ):
    if setBit:
    	return taken | (1 << itemIdx)
    else:
        return taken & ~(1 << itemIdx)

def recursive_test( capacity, items, min_needed ):
    if ( len(items) > 0 ):
        max_possible = simple_packing( capacity, items )
        if ( min_needed <= max_possible ):
            without_results = recursive_test( capacity, items[1:], min_needed )
            if ( capacity >= items[0].weight ):
	        temp = recursive_test( capacity - items[0].weight, items[1:], min_needed )
	        with_results = ( temp[0]+items[0].value,temp[1]+items[0].weight, temp[2]+ 2 ** items[0].index )
                if ( with_results[0] >= without_results[0] ):
		    return with_results
	        else:
		    return without_results
            return without_results
    return (0,0,0)

def output_bits( items, taken ):
    output = ""
    bitmask = 1
    for x in xrange( 0,len(items) ):
	if taken & bitmask:
	    output += " 1"
        else:
            output += " 0"
        bitmask <<= 1
    return output[ ::-1 ]

def simple_packing( capacity, items, taken_not_allowed = 0 ):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = 0

    for item in items:
        if weight + item.weight <= capacity:
            if not ( 1 << item.index & taken_not_allowed ):
	        taken = set_taken( taken, item.index, True )
        	value += item.value
                weight += item.weight
                if ( weight == capacity ):
                    break
    return value, weight, taken
    
# capacity is amount of room to populate
# items are available space
# taken not allowed is the item indices that we will not allow as part of the selected
def best_possible( capacity, items, taken_not_allowed=0 ):
    value, weight, taken = simple_packing( capacity, items, taken_not_allowed )
    free_space = float(capacity - weight)
    best_attempt = (value,weight,taken)
    for item in items:
        print "Item: ",str(item)
        item_bitmask = 1 << item.index
        if ( is_taken( taken, item.index ) ):
            next_try = simple_packing( capacity, items, item_bitmask )
            print "Next Try: ",str(next_try), "  BitMask: ", str(item_bitmask)
            if ( next_try[0] > best_attempt[0] ):
                best_attempt = next_try
    return best_attempt

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    capacity, items = format_data(lines)
    sorted( items, key=lambda item: -(float(item.value)/item.weight) )

    print "Capacity: ",capacity
    for item in items:
	print item, (float(item.value)/item.weight)

    print "Recursive Max: ", str( recursive_test( capacity, items, 0 ) )

    print "Best Possible: ",str(best_possible(capacity,items))
    value, weight, taken = simple_packing( capacity, items )
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
#    output_data += ' '.join(map(str, taken))
    output_data += output_bits( items, taken )

    value2, weight2, taken2 = best_possible( capacity, items )
    output_data2 = str(value2) + ' ' + str(0) + '\n'
#    output_data += ' '.join(map(str, taken))
    output_data2 += output_bits( items, taken2 )

    print "Output Data2: ",output_data2

    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

