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

def output_bits( items, taken ):
    output = ""
    bitmask = 1
    for x in xrange( len(items) ):
	if taken & bitmask:
	    output += " 1"
        else:
            output += " 0"
        taken = taken >> 1
    return output[ ::-1 ]

def simple_packing( capacity, items ):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = 0

    for item in items:
        if weight + item.weight <= capacity:
            taken = set_taken( taken, item.index, True )
            value += item.value
            weight += item.weight
    return value, weight, taken
    
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    capacity, items = format_data(lines)
    value, weight, taken = simple_packing( capacity, items )
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
#    output_data += ' '.join(map(str, taken))
    output_data += output_bits( items, taken )

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

