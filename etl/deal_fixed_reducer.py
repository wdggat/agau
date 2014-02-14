#!/usr/bin/env python

import sys
import utils
from agau import Agau

def reducer(lines, threshold):
    dealed = {}
    for line in lines:
        agtd = Agau.get_from_agauline(line)
        if utils.at_night(agtd.dt) and not utils.at_bid_time(agtd.dt):
	    if threshold > 0 and agtd.price - agtd.open_price >= threshold and dealed.get(agtd.day, '-') == '-':
	        dealed[agtd.day] = agtd.time
	    if threshold < 0 and agtd.price - agtd.open_price <= threshold and dealed.get(agtd.day, '+') == '+':
	        dealed[agtd.day] = agtd.time
	    
    i = 1
    print '%s\t%s\t\t%s' % ('NO', 'DAY', 'TIMESTAMP')
    for day in sorted(dealed.keys()):
        print '%s\t%s\t%s' % (i, day, dealed.get(day))
	i += 1

if __name__ == '__main__':
    reducer(sys.stdin, int(sys.argv[1]))

