#!/usr/bin/python
# -*- coding: utf-8 -*-

# pass in text of file as a single line
# returns node_count, edge_count, edges tuple
def parse_it(input_data):
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    return(node_count, edge_count, edges, line, parts) 

# break down the edges and return a dictionary with key as node number, contents list of nodes connected to
def create_nodes( node_cnt, edges ):
    nodes = dict()
    for i in range(0,node_cnt):
        nodes[i] = []
    for edge in edges:
        # append edge 1 to the current list of edges connected to node[edge[0]]
        nodes[edge[0]].append(edge[1])
        nodes[edge[1]].append(edge[0])
    return nodes

def get_used_colors(colors, ends):
    used_colors = set()
    for end in ends:
        if ( colors[end] != -1 ):
            used_colors.add(colors[end])
    return used_colors

# We'll use a dictionary to store nodeIdx as key and a Set of Nodes we connect to
# Colors in use will store the number of colors we are using
# We'll create a set
def color_it( node_cnt, edges ):
    nodes = create_nodes( node_cnt, edges )
    colors = [-1]*node_cnt
    max_color_used = -1
    print "Nodes: ",str(nodes)
    max_color_used += 1
    colors[0] = max_color_used
    for nodeIdx in nodes:
        used_colors = get_used_colors(colors, nodes[ nodeIdx ] )
        if ( colors[ nodeIdx ] == -1 ):
            for test_color in xrange(0,max_color_used):
                print "NodeIdx: ",str(nodeIdx)
                print "Node[nodeidx]: ",str(nodes[nodeIdx])
                if ( test_color not in used_colors ):
                    colors[nodeIdx] = test_color
                    break
            if ( colors[nodeIdx] == -1 ):
                max_color_used += 1
                colors[nodeIdx] = max_color_used

    return max_color_used, colors

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    node_count, edge_count, edges, line, parts = parse_it(input_data)

    # build a trivial solution
    # every node has its own color
#    solution = range(0, node_count)
    solution = color_it(node_count,edges)

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

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
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

