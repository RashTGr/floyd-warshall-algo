# Floyd Warshall Algorithm - imperative version

import sys

import itertools

# Global variables of the function
no_path = sys.maxsize 
max_length = len(graph[0]) 

"""Variable 'no_path' indicates that no direct path exists."""


"Algorithm "
def floyd_imperative_pdf(distance): 
    """This is imperative verion of algorithm based 
    on the solution provided in the course materials.
    Distance will be the output matrix with the 
    shortest distances between each pair of nodes."""

    for intermediate, start_node, end_node\
        in itertools.product\
            (range(max_length), range(max_length), range(max_length):



graph = [[]]