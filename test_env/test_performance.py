import timeit

from numpy import inf

import floyd_algo_imp as imp

import floyd_algo_rec as rec


# Global variable to test performance
matrix = [
    [0, 5, inf, 10],
    [inf, 0, 3, inf],
    [inf, inf, 0, 1],
    [inf, inf, inf, 0]
    ]


def imperative_performance():
    imp.floyd_imperative(matrix)
        
def recursive_performance():
    rec.floyd_recursive(matrix)
"""Defining both of the called functions 
to pass performance tests.
"""


# 'Minimum' runtime of performance tests
imperative_min = min(timeit.repeat(imperative_performance, number=1000))

recursive_min = min(timeit.repeat(recursive_performance, number=1000))

print("'Min' execution time: ", "\n", " - imperative: ", 
imperative_min, "\n", " - recursive : ", recursive_min)



# 'Maximum' runtime of performance tests
imperative_max = max(timeit.repeat(imperative_performance, number=1000))

recursive_max = max(timeit.repeat(recursive_performance, number=1000))

print("'Max' execution time: ", "\n", " - imperative: ", 
imperative_max, "\n", " - recursive : ", recursive_max)



# Boost the number of iterations.
imperative_avr = timeit.timeit(imperative_performance, number=7000)

recursive_avr = timeit.timeit(recursive_performance, number=7000)

print("Average execution time: ", "\n", " - imperative: ", 
imperative_avr, "\n", " - recursive : ", recursive_avr)



if __name__ == "__main__":
    print("Performance Tests for 'Imperative' and 'Recursive' functions")