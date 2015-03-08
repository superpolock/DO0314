#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight', 'ratio'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    print "Capacity: " + format(capacity)
    items = []
    maximumValue = 0.0

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        value = int(parts[0])
        maximumValue += value
        weight =  int(parts[1])
        items.append(Item(i-1, value, weight,float(value)/weight))

    # Filling the knapsack in order based on the most value dense items
    value = 0
    weight = 0
    taken = [0]*len(items)

    items = sorted(items,key=lambda item:-item.ratio)
    for item in items:
        print item

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
            if weight == capacity:
                break
        else:
            remainingSpace = capacity - weight
            maximumValue = value + (item.value * (remainingSpace/item.weight))
            print "MaximumValue: "+str(maximumValue)

    # tree to find best value
    # 
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
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

