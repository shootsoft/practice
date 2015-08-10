__author__ = 'yinjun'

import unittest
import os
import imp
import random

class CombineTests(unittest.TestCase):
    def setUp(self):
        path = os.getcwd() + '/KPoint.py'
        so = imp.load_source('KPoint', path)
        self.s = so.KPoint(10)

    def test_Point(self):
        path = os.getcwd() + '/KPoint.py'
        so = imp.load_source('Point', path)
        actual = so.Point(3,4)
        self.assertEqual("(3, 4)", str(actual))
        self.assertEqual(5, actual.getDistance())

    def test_KPoints(self):

        points = [[32, -35], [-18, 58], [21, -54], [-13, -66], [-91, -67], [-84, 16], [70, -21], [-84, -96], [-48, -95], [16, -15], [-58, -100], [56, 12], [-52, 38], [-64, -70], [-42, 1], [-97, -8], [69, 93], [38, -88], [36, -88], [-81, 1], [0, -57], [-65, -87], [13, 61], [-22, -47], [31, 60], [-36, -68], [99, -16], [100, -2], [62, 45], [-7, 54], [99, -14], [48, -38], [-76, -24], [-74, -17], [91, -7], [-32, 4], [-70, 59], [96, 3], [-15, -35], [-7, 48], [-12, -42], [30, -89], [-66, -92], [-50, 57], [-51, 36], [1, 35], [-34, 6], [37, 37], [-92, 1], [-6, -35], [-33, -66], [-58, 96], [-25, 1], [-69, -79], [29, 88], [-17, -90], [67, -5], [-85, -6], [-95, -73], [-61, 48], [-13, 37], [-17, 38], [60, 91], [-86, 21], [-66, 64], [-99, 35], [-50, -45], [10, 95], [62, -80], [-63, -28], [71, 52], [86, 82], [-100, 100], [-60, 48], [-43, -55], [-65, -35], [-40, -93], [88, -7], [-36, 100], [60, 31], [1, 82], [-7, 78], [-75, -13], [35, 9], [5, 81], [19, 5], [82, 52], [-10, -65], [-89, 93], [-27, 56], [86, -37], [96, -29], [42, -28], [-47, -3], [65, 69], [71, -58], [-3, 93], [-33, -22], [64, -30], [26, -32]]
        expected = str([(19,5), (16,-15), (-25,1), (-32,4), (-34,6)])
        actual = str(self.s.getKpoints(points, 5))
        self.assertEqual(expected, actual)

        expected = str([(19, 5), (16, -15), (-25, 1), (-32, 4), (-13, 37), (-33, -22), (26, -32), (-42, 1), (-22, -47), (-50, -45), (-34, 6), (35, 9), (-15, -35), (-17, 38), (32, -35), (-47, -3), (-7, 54), (56, 12), (-63, -28), (1, 35), (-12, -42), (42, -28), (21, -54), (0, -57), (48, -38), (67, -5), (60, 31), (-43, -55)])
        actual = str(self.s.getKpoints(points, 20))
        self.assertEqual(expected, actual)

# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(CombineTests)
    unittest.TextTestRunner(verbosity=2).run(suite)