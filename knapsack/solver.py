#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight', 'ratio'])

def greatestPossible( capacity, items, taken):
    value = 0
    weight = 0.0
    for item in items:
        if ( item.weight < capacity ):
            if ( weight + item.weight <= capacity ):
                value += item.value
                optimalValue = value
                weight += item.weight
            else:
                spaceAvailable = capacity - weight
                optimalValue = value + float(spaceAvailable)*item.value/item.weight
                break
    return optimalValue

# returns a tuple of value, taken
def fill_it(capacity, items):
    # Filling the knapsack in order based on the most value dense items
    value = 0
    weight = 0
    taken = [0]*len(items)

    items = sorted(items,key=lambda item:-item.ratio)
    for item in items:
        print item

    maximumValue = greatestPossible( capacity, items, taken )
    print "MaximumValue: "+str(maximumValue)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
            if weight == capacity:
                break
    return(value,taken)

def recursive_fill(capacity, items):
    if ( capacity > 0 ):
        if ( len(items) > 0 ):
            valueWith, takenWith = fill_it(capacity - items[0].weight, items[1:] )
            valueWith = valueWith + items[0].value
            takenWith[items[0].index] = 1
            valueWithout, takenWithout = fill_it( capacity, items[1:] )
            valueSet = True
            if ( valueWith > valueWithout ):
                return (valueWith, takenWith)
            else:
                return(valueWithout,takenWithout)
    return fill_it( capacity, items )

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    print "Capacity: " + format(capacity)
    items = []
    maximumValue = 0

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        value = int(parts[0])
        weight =  int(parts[1])
        items.append(Item(i-1, value, weight,float(value)/weight))

    print "Total of all items: "+str(maximumValue)

    # tree to find best value
    # 
    value, taken = fill_it(capacity, items)

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))

    recursiveValue, takenValue = recursive_fill(capacity,items)
    print("RecusiveValue: "+str(recursiveValue))
    print( ' '.join(map(str,takenValue)))

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

