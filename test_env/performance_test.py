import timeit

from numpy import inf

import floyd_algo_imp as imp

import floyd_algo_rec as rec

matrix = [
    [0, 5, inf, 10],
    [inf, 0, 3, inf],
    [inf, inf, 0, 1],
    [inf, inf, inf, 0]
    ]

def FloydPerformance():
    #time1 = rec.floyd_recursive(matrix)
    time2 = imp.floyd_imperative(matrix)

    return time2

imp_performance = timeit.timeit(FloydPerformance, number=100)
print(imp_performance)

#print(FloydPerformance())