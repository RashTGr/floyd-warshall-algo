# Floyd Warshall Algorithm - recursive version

import sys

import numpy as np

from numpy import inf

sys.setrecursionlimit(999)


"""Algorithm implementation"""
def floyd_recursive(distance, n):

    """ 'distance' and 'n' are parameters of function, 
    where 'n' is the number of nodes in the graph, and
    it is linked to the length of graph to avoid manual input."""
    """The 'distance' will contain the values that represent 
    the shortest distances between each pair of nodes."""
    
    distance = graph

    """[i] represents 'start node' or rows and [j] represents 
    'end node' or columns, whereas 'k' is the intermediate node."""
    for k in range(n):
        for i in range(n):
            for j in range(n):

                # Base case
                if i == j: 
                    distance[i][j] == 0
                elif k and i and j >= inf:
                    distance[i][j] == inf # Means no direct path exists
                
                # Recursive case
                # Setting each node as an intermediate node in pair with 'k'.
                else: 
                    distance[i][j] = min(distance[i][j], 
                                         distance[i][k] + distance[k][j])

    return np.matrix(distance)
        
   

# Input data, matrix
graph = [[0, 5, inf, 10],
         [inf, 0, 3, inf],
         [inf, inf, 0, 1],
         [inf, inf, inf, 0]
        ]

# Function call and print the solution
print(floyd_recursive(graph, n=len(graph)))
