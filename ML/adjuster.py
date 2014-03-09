#!/usr/bin/env python 

def Adjuster():
    #reference: the index of the reference value for comparison
    def __init__(self, reference, value_len, domain, denominators, ave_cost_need):
        self.reference = reference
	self.domain = domain
	self.value_len
	self.denominators = denominators
	self.ave_cost_need = ave_cost_need

STAGE_2 = Adjuster(-1, 2, [(-100, 100)] + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100)
STAGE_3 = Adjuster(-1, 2, [(-100, 100)] * 2 + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100)
STAGE_4 = Adjuster(-1, 2, [(-100, 100)] * 3 + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100)
STAGE_5 = Adjuster(-1, 2, [(-100, 100)] * 4 + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100)
STAGE_6 = Adjuster(-1, 2, [(-100, 100)] * 5 + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100)

def get_adjuster(name):
    if name == 'STAGE_2':
        return STAGE_2
    if name == 'STAGE_3':
        return STAGE_3
    if name == 'STAGE_4':
        return STAGE_4
    if name == 'STAGE_5':
        return STAGE_5
    if name == 'STAGE_6':
        return STAGE_6

