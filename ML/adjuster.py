#!/usr/bin/env python 

class Adjuster():
    #reference: the index of the reference value for comparison
    def __init__(self, reference, value_len, domain, denominators, ave_cost_need):
        self.reference = reference
	self.domain = domain
	self.value_len = value_len
	self.denominators = denominators
	self.ave_cost_need = ave_cost_need

adjusters = {
  'STAGE_2' : Adjuster(-1, 2, [(-100, 100)] + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100),
  'STAGE_3' : Adjuster(-1, 3, [(-100, 100)] * 2 + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100),
  'STAGE_4' : Adjuster(-1, 4, [(-100, 100)] * 3 + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100),
  'STAGE_5' : Adjuster(-1, 5, [(-100, 100)] * 4 + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100),
  'STAGE_6' : Adjuster(-1, 6, [(-100, 100)] * 5 + [(-2000, 2000)], [20 * (i+1) for i in range(10)], 100),
  'EXAMINE_NO22' : Adjuster(1, 5, [(-100, 100)] * 4 + [(-2000, 2000)], [5 * (i+1) for i in range(40)], 1000),
  'EXAMINE_WITH22' : Adjuster(1, 6, [(-100, 100)] * 5 + [(-2000, 2000)], [5 * (i+1) for i in range(40)], 1000),
}

def get_adjuster(name):
    return adjusters.get(name)

