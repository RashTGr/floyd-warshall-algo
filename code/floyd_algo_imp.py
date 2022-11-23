# Floyd Warshall Algorithm - imperative version

import sys

import itertools


# Any value that have 'sys.maxsize' has no path
no_path = sys.maxsize 

# The example graph
graph = [
    [0, 7, no_path, 8],
    [no_path, 0, 5, no_path],
    [no_path, no_path, 0, 2],
    [no_path, no_path, no_path, 0]
    ]

# Number of nodes in the graph
max_length = len(graph[0]) 


def floyd_imperative(distance): 
    
    """This is imperative verion of algorithm based 
    on the solution provided in the course materials.
    Distance will be the output graph with the 
    shortest distances between each pair of nodes."""


    for intermediate, start_node, end_node\
        in itertools.product\
            (range(max_length), range(max_length), range(max_length)): 

            # Assume that if start_node and end_node are the same
            # then the distance would be zero
            if start_node == end_node:
                distance[start_node][end_node] = 0
                continue

            # Return all possible paths and find the minimum
            distance[start_node][end_node] = min(distance[start_node][end_node], 
                                             distance[start_node][intermediate] 
                                           + distance[intermediate][end_node])
    #Print solution
    print(distance)

#Function call
floyd_imperative(graph)