__author__ = 'yinjun'

import unittest
import os
import imp


class TestSolutionFuncs(unittest.TestCase):
    def setUp(self):
        path = os.getcwd() + '/solution.py'
        so = imp.load_source('solution', path)
        self.s = so.Solution()

        # common = os.path.dirname(os.path.dirname(os.getcwd())) + '/common/listnode.py'
        #print common
        #listnode = imp.load_source('listnode', common)
        #self.listnode = listnode.ListNode(0)

    def test_nthUglyNumber(self):
        expected = 1
        actual = self.s.nthUglyNumber(1)
        self.assertEqual(expected, actual)

        expected = 2
        actual = self.s.nthUglyNumber(2)
        self.assertEqual(expected, actual)

        expected = 3
        actual = self.s.nthUglyNumber(3)
        self.assertEqual(expected, actual)

        expected = 4
        actual = self.s.nthUglyNumber(4)
        self.assertEqual(expected, actual)


        expected = 5
        actual = self.s.nthUglyNumber(5)
        self.assertEqual(expected, actual)


        expected = 6
        actual = self.s.nthUglyNumber(6)
        self.assertEqual(expected, actual)


        expected = 8
        actual = self.s.nthUglyNumber(7)
        self.assertEqual(expected, actual)


        expected = 9
        actual = self.s.nthUglyNumber(8)
        self.assertEqual(expected, actual)


        expected = 10
        actual = self.s.nthUglyNumber(9)
        self.assertEqual(expected, actual)


        expected = 12
        actual = self.s.nthUglyNumber(10)
        self.assertEqual(expected, actual)

        expected = 15
        actual = self.s.nthUglyNumber(11)
        self.assertEqual(expected, actual)


# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)

