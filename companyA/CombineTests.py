__author__ = 'yinjun'

import unittest
import os
import imp


class CombineTests(unittest.TestCase):
    def setUp(self):
        path = os.getcwd() + '/Combine.py'
        so = imp.load_source('Combine', path)
        self.s = so.Combine()


    def test_calculate_combinations(self):

        expected = [[1, 1], [1, 1], [1, 1]]
        actual = self.s.calculate_combinations([1, 1, 1], 2)
        self.assertEqual(expected, actual)

        expected = [[5, 10], [5, 10], [15]]
        actual = self.s.calculate_combinations([5, 5, 15, 10], 15)
        self.assertEqual(expected, actual)


        expected = [[1,1,1,1,1,1]]
        actual = self.s.calculate_combinations([1,1,1,1,1,1], 6)
        self.assertEqual(expected, actual)

        expected = [[1, 1, 1, 1, 1],  [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],  [1, 1, 1, 1, 1],  [1, 1, 1, 1, 1],  [1, 1, 1, 1, 1]]
        actual = self.s.calculate_combinations([1,1,1,1,1,1], 5)
        self.assertEqual(expected, actual)

        expected = []
        actual = self.s.calculate_combinations([], 1)
        self.assertEqual(expected, actual)

        expected = []
        actual = self.s.calculate_combinations([], None)
        self.assertEqual(expected, actual)

        expected = []
        actual = self.s.calculate_combinations(None, 0)
        self.assertEqual(expected, actual)

        expected = []
        actual = self.s.calculate_combinations([1], 2)
        self.assertEqual(expected, actual)

        expected = [[1, 1]]
        actual = self.s.calculate_combinations([1, 1], 2)
        self.assertEqual(expected, actual)

        expected = [[1, 1, 1]]
        actual = self.s.calculate_combinations([1, 1, 1], 3)
        self.assertEqual(expected, actual)


        expected = [[5, 9],  [6, 8],  [1, 4, 9],  [1, 5, 8],  [1, 6, 7],  [1, 2, 3, 8],  [1, 2, 4, 7],  [1, 2, 5, 6],  [1, 3, 4, 6],  [2, 3, 9],  [2, 4, 8],  [2, 5, 7],  [2, 3, 4, 5],  [3, 4, 7],  [3, 5, 6]]
        actual = self.s.calculate_combinations([1,2,3,4,5,6,7,8,9], 14)
        self.assertEqual(len(expected), len(actual))

        expected = [[5, 9],  [6, 8],  [-2, 7, 9],  [-2, -1, 8, 9],  [-2, -1, 3, 5, 9],  [-2, -1, 3, 6, 8],  [-2, -1, 4, 5, 8],  [-2, -1, 4, 6, 7],  [-2, 3, 4, 9],  [-2, 3, 5, 8],  [-2, 3, 6, 7],  [-2, 4, 5, 7],  [-1, 6, 9],  [-1, 7, 8],  [-1, 3, 4, 8],  [-1, 3, 5, 7],  [-1, 4, 5, 6],  [3, 4, 7],  [3, 5, 6]]
        actual = self.s.calculate_combinations([-2, -1, 3, 4, 5, 6, 7, 8, 9], 14)
        self.assertEqual(len(expected), len(actual))

        expected = [[0],  [0, 1, -1],  [0, 1, -1, 0],  [0, 1, -1, 0, -1, 1],  [0, 1, -1, -1, 1],  [0, 1, 0, -1],  [0, 1, -1],  [0, -1, 0, 1],  [0, -1, 1],  [0, 0],  [0, 0, -1, 1],  [0, -1, 1],  [1, -1],  [1, -1, 0],  [1, -1, 0, -1, 1],  [1, -1, -1, 1],  [1, 0, -1],  [1, -1],  [-1, 0, 1],  [-1, 1],  [0],  [0, -1, 1],  [-1, 1]]
        actual = self.s.calculate_combinations([0, 1, -1, 0 ,-1, 1], 0)
        self.assertEqual(expected, actual)




# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(CombineTests)
    unittest.TextTestRunner(verbosity=2).run(suite)