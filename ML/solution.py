#!/usr/bin/env python

class Solution():
    def __init__(self, denominator, resolve, ave_cost, LENGTH, SAME):
        self.denominator = denominator
	self.resolve = resolve
	self.ave_cost = ave_cost
	self.LENGTH = LENGTH
	self.SAME = SAME
        
    def __str__(self):
	return 'denominator: %d, resolve: %s, ave_cost: %f, LENGTH: %d, SAME: %f' % (self.denominator, self.resolve, self.ave_cost, self.LENGTH, self.SAME)

    @classmethod
    def EMPTY():
        return Solution(0, None, 0, 0, 0)
	
