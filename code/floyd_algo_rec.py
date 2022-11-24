"""Floyd Warshall Algorithm - recursive version."""

"""This is a shortest path algorithm for all possible 
pair-combinations.
"""

import sys

import numpy as np

from numpy import inf

sys.setrecursionlimit(999)


# Algorithm implementation
def floyd_recursive(distance):
    """The 'distance' will contain the values that represent 
    the shortest distances between each pair of nodes.
    """
    
    length = len(graph)
    """The 'length' is the number of nodes in the graph, 
    and is linked to the length of graph to avoid manual input.
    """
    
    distance = graph


    for k in range(length):
        for i in range(length):
            for j in range(length):
                """'i' represents 'start node' or rows and 'j' 
                represents 'end node' or columns, whereas 'k' is 
                the intermediate node.
                """

                # Base case
                if i == j: 
                    distance[i][j] == 0

                # Infinity is defined as the largest possible value.
                elif k and i and j >= inf:
                    distance[i][j] == inf 
                    """'inf' stands for infinity and means 
                    no direct path exists.
                    """
                
                # Recursive case
                else: 
                    distance[i][j] = min(distance[i][j], 
                                         distance[i][k] + distance[k][j])
                """Setting each node as an intermediate node in pair 
                with 'k'.  If the shortest path from 'i' to 'j' passes 
                through 'k', then the value of distance[i][j] should 
                be updated accordingly.
                """
    # Returns the shortest path
    return np.array(distance)
   

# Input data, matrix
graph = [[0, 5, inf, 10],
         [inf, 0, 3, inf],
         [inf, inf, 0, 1],
         [inf, inf, inf, 0]
        ]

print(floyd_recursive(graph))
"""This is to call function and print the solution."""
