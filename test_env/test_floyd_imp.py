# Docstring

""" Change all data to imperative method """

import sys

import unittest

import floyd_algo_imp as imperative

no_path = sys.maxsize

class FloydImpTest(unittest.TestCase): 

    def setUp(self):
        self.input_1 =  [
            [0, 7, no_path, 8], 
            [no_path, 0, 5, no_path], 
            [no_path, no_path, 0, 2], 
            [no_path, no_path, no_path, 0]
            ]
        
        self.output_1 = [
            [0,  7, 12,  8],
            [no_path,  0,  5,  7], 
            [no_path, no_path,  0,  2], 
            [no_path, no_path, no_path,  0]
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

    def tearDown(self):
        self.input_1 = 0
        self.output_2 = 0
        self.input_2 = 0
        self.output_2 = 0


    def test_floyd_imp1(self):
        self.assertEqual(imperative.floyd_imperative(self.input_1), self.output_1)
        self.assertEqual(imperative.floyd_imperative(self.input_2), self.output_2)
    
    # To make this test better adding in additional checks
    def test_floyd_imp2(self):
        self.assertEqual(imperative.floyd_imperative(self.input_2), self.output_2)
        self.assertEqual(imperative.floyd_imperative(self.input_1), self.output_1)


if __name__ == "__main__":
    unittest.main()