#!/usr/bin/env python 

import sys
import utils
from agau import Agau 

# ag = a * au + b
def reducer(lines):
    ag_dealed, au_dealed, ags, ag_price = set(), set(), {}, 0
    for line in lines:
        agtd = Agau.get_from_agauline(line)
	if agtd.kind == 'Ag(T+D)' and agtd.time not in ag_dealed:
	    ag_price = agtd.price
	    ag_dealed.add(agtd.time)
	elif agtd.kind == 'Au(T+D)' and agtd.time not in au_dealed:
	    ags.setdefault(ag_price, [])
	    ags[ag_price].append(agtd.price)
	    au_dealed.add(agtd.time)

    for ag in sorted(ags.keys()):
        print '%s\t%s' % (ag, ags[ag])
#        aver = average(ags[ag])
#	if aver != 0:
#            print '%s\t%s' % (ag, aver)

def average(scores):
    s,num = 0,0
    for score in scores:
        if score == 0: continue
	s += score 
	num += 1
    if num == 0: return 0
    return s/num
        
def print_usage():
    print "grep -P 'T\+D' ../agau.dat | python ag_au_mappings.py"

if __name__ == '__main__':
    reducer(sys.stdin)

