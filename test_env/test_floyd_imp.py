"""This is Unit testing of 'Imperative' function for 
Floyd-Warshall algorithm.
"""

import sys

import unittest

import floyd_algo_imp as imperative


# Global variable
no_path = sys.maxsize


class FloydImpTest(unittest.TestCase): 
    """Implementing TestCase class of 'unittest' module."""
    
    # Setting up data to be used in testing
    def setUp(self):
        self.input_1 = [
            [0, 7, no_path, 8], 
            [no_path, 0, 5, no_path], 
            [no_path, no_path, 0, 2], 
            [no_path, no_path, no_path, 0]
            ]
        
        self.output_1 = [
            [0, 7, 12, 8],
            [no_path, 0, 5, 7], 
            [no_path, no_path, 0, 2], 
            [no_path, no_path, no_path, 0]
            ]

        self.input_2 = [
            [0, 5, no_path, 10],
            [no_path, 0, 3, no_path],
            [no_path, no_path, 0, 1],
            [no_path, no_path, no_path, 0]
            ]
            
        self.output_2 = [
            [0, 5, 8, 9], 
            [no_path, 0, 3, 4], 
            [no_path, no_path, 0, 1], 
            [no_path, no_path, no_path, 0]
            ]
    
    # Method to be called after each 
    # test case to cleanup generated data
    def tearDown(self):
        self.input_1 = 0
        self.output_2 = 0
        self.input_2 = 0
        self.output_2 = 0

    def test_floyd_imp1(self):
        self.assertEqual(imperative.floyd_imperative(self.input_1), self.output_1)
        self.assertEqual(imperative.floyd_imperative(self.input_2), self.output_2)
        """Implementation of 'assertEqual' method of TestCase class."""
    
    # To make this test better adding in additional checks
    def test_floyd_imp2(self):
        self.assertEqual(imperative.floyd_imperative(self.input_2), self.output_2)
        self.assertEqual(imperative.floyd_imperative(self.input_1), self.output_1)


# Informative print statement
print("Unit Test for 'Imperative' function!")

if __name__ == "__main__":
    unittest.main()