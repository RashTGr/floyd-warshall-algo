"""Floyd Warshall Algorithm with recursive function."""

"""This is a shortest path algorithm for all possible 
pair-combinations.
"""

import sys

import numpy as np

from numpy import inf

sys.setrecursionlimit(999)


# Algorithm implementation
def floyd_recursive(matrix):
    """The 'matrix' will contain the values that represent 
    the shortest distance between each pair of nodes.
    """
    
    length = len(matrix)
    """The 'length' is the number of nodes, and is linked 
    to the length of matrix to avoid manual input.
    """


    for k in range(length):
        for i in range(length):
            for j in range(length):
                """'i' represents 'start node' or rows and 'j' 
                represents 'end node' or columns, whereas 'k' is 
                the intermediate node.
                """

                # Base case
                if i == j: 
                    matrix[i][j] == 0

                # Infinity is defined as the largest possible value.
                elif k and i and j >= inf:
                    matrix[i][j] == inf 
                    """'inf' stands for infinity and means 
                    no direct path exists.
                    """
                
                # Recursive case
                else: 
                    matrix[i][j] = min(matrix[i][j], 
                                       matrix[i][k] + matrix[k][j])
                """Setting each node as an intermediate node in pair 
                with 'k'.  If the shortest path from 'i' to 'j' 
                passes through 'k', then the value of matrix[i][j] 
                should be updated accordingly.
                """
    # Returns the shortest path
    return matrix
   

# Input data
matrix = [
    [0, 5, inf, 10],
    [inf, 0, 3, inf],
    [inf, inf, 0, 1],
    [inf, inf, inf, 0]
    ]


if __name__ == "__main__":
    # Function call
    floyd_recursive(matrix)
    # and print solution
    print(np.array(floyd_recursive(matrix)))