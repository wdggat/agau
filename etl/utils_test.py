#!/usr/bin/env python 

import unittest
import utils

class UtilTest(unittest.TestCase):
    def test_subsets(self):
        s = [1,2,3]
	expected = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
	actual = utils.subsets(s)
	#print 'actual: %s' % actual
        self.assertItemsEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

