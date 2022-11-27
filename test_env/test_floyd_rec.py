"""This is Unit testing of 'Recursive' function for 
Floyd-Warshall algorithm.
"""

import unittest

from numpy import inf

import floyd_algo_rec as recursive


class FloydRecTest(unittest.TestCase): 
    """Implementing TestCase class of 'unittest' module."""
    
    # Setting up data to be used in testing
    def setUp(self):
        self.input_1 = [
            [0, 7, inf, 8], 
            [inf, 0, 5, inf], 
            [inf, inf, 0, 2], 
            [inf, inf, inf, 0]
            ]
        
        self.output_1 = [
            [0, 7, 12, 8],
            [inf, 0, 5, 7], 
            [inf, inf, 0, 2], 
            [inf, inf, inf, 0]
            ]

        self.input_2 = [
            [0, 5, inf, 10],
            [inf, 0, 3, inf],
            [inf, inf, 0, 1],
            [inf, inf, inf, 0]
            ]
            
        self.output_2 = [
            [0, 5, 8, 9], 
            [inf, 0, 3, 4], 
            [inf, inf, 0, 1], 
            [inf, inf, inf, 0]
            ]
    
    # Method to be called after each 
    # test case to cleanup generated data
    def tearDown(self):
        self.input_1 = 0
        self.input_2 = 0
        self.output_1 = 0
        self.output_2 = 0

    def test_floyd_1(self): 
        self.assertEqual(recursive.floyd_recursive(self.input_1), self.output_1)
        self.assertEqual(recursive.floyd_recursive(self.input_2), self.output_2)
        """Implementation of 'assertEqual' method of TestCase class."""

    # To make this test better adding in additional checks
    def test_floyd_2(self):
        self.assertEqual(recursive.floyd_recursive(self.input_2), self.output_2)
        self.assertEqual(recursive.floyd_recursive(self.input_1), self.output_1)


# Informative print statement
print("Unit Test for 'Recursive' function!")

if __name__ == "__main__": 
    unittest.main()