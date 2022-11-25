# def add (x, y):
#     return x + y

# def subtract(x, y): 
#     return x - y

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         raise ValueError('Cannot divide by zero!')
#     return a / b

from numpy import inf
import numpy as np

input =  [
    [0, 7, inf, 8],
    [inf, 0, 5, inf],
    [inf, inf, 0, 2],
    [inf, inf, inf, 0]
    ]

output = [
    [0,  7, 12,  8],
    [inf,  0,  5,  7],
    [inf, inf,  0,  2],
    [inf, inf, inf,  0]
    ]

input2 = [
    [0, 5, inf, 10],
    [inf, 0, 3, inf],
    [inf, inf, 0, 1],
    [inf, inf, inf, 0]
    ]

output2 = [
    [0, 5, 8, 9], 
    [inf, 0, 3, 4], 
    [inf, inf, 0, 1], 
    [inf, inf, inf, 0]
    ]

""" output = [
    [0, 7, 12, 8], 
    [9223372036854775807, 0, 5, 7], 
    [9223372036854775807, 9223372036854775807, 0, 2], 
    [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]
    ] """
