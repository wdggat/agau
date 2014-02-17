#!/usr/bin/env python

import sys
import utils
from agau import Agau

#NO	DAY		NIGHT^	NIGHT$	AM^	AM$	PM^	PM$
def reducer(lines):
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ('NO', 'DAY', '--NIGHT^', 'NIGHT$-^', '--AM^', 'AM^-$', '--PM^', 'PM^-$')
    last_pm_end,night_bid = 0, ''
    for line in lines:
        items = line.strip().split('\t')
	if len(items) == 8:
	    night_begin = float(items[2])
	    night_end = float(items[3])
	    am_begin = float(items[4])
	    am_end = float(items[5])
	    pm_begin = float(items[6])
	    pm_end = float(items[7])
	    if last_pm_end != 0:
	        night_bid = utils.substract(night_begin, last_pm_end);
	    if night_begin == 0:
	        night_bid = ''
	    last_pm_end = pm_end
	        
            print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (items[0], items[1], night_bid, utils.substract(night_end, night_begin, ''), utils.substract(am_begin, night_end, ''), utils.substract(am_end, am_begin, ''), utils.substract(pm_begin, am_end, ''), utils.substract(pm_end, pm_begin, ''))

def print_usage():
    print 'Usage:'
    print '\tcat boundary_prices.txt | python stage_alter_direction.py'

if __name__ == '__main__':
    reducer(sys.stdin)
  
