import unittest

import file1

class TestFile(unittest.TestCase):

    def test_add(self):        
        self.assertEqual(file1.add(10, 5), 15)
        self.assertEqual(file1.add(-1, 1), 0)
        self.assertEqual(file1.add(-1, -1), -2)


    def test_subt(self):
        self.assertEqual(file1.subtract(10, 5), 5)
        self.assertEqual(file1.subtract(-2, -3), 1)
        self.assertEqual(file1.subtract(10, 3), 7)


    def test_multip(self):
        self.assertEqual(file1.multiply(10, 5), 50)
        self.assertEqual(file1.multiply(-2, -3), 6)
        self.assertEqual(file1.multiply(10, 3), 30)


    def test_div(self):
        self.assertEqual(file1.divide(10, 5), 2)
        self.assertEqual(file1.divide(-6, -3), 2)
        self.assertEqual(file1.divide(21, 3), 7)

if __name__ == '__main__':
    unittest.main()

