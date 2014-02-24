#!/usr/bin/env python
#-*-coding: utf8-*-

import sys
import utils
from paper import Paper 

BEGIN, END = (13, 30), (21, 0)
def reducer(lines):
    begins, ends = {}, {}
    for line in lines:
        gold = Paper.get_from_paperline(line)
	if gold.day not in begins and (gold.dt.hour > BEGIN[0] or (gold.dt.hour == BEGIN[0] and gold.dt.minute >= BEGIN[1])):
	    begins[gold.day] = gold.price
	elif gold.dt.hour < END[0] or (gold.dt.hour == END[0] and gold.dt.minute <= END[1]):
	    ends[gold.day] = gold.price 

    for day in sorted(begins.keys()):
        if day not in ends: continue
        print '%s\t%s' % (day, ends[day] - begins[day])

def print_usage():
    print 'grep -e "美元账户黄金" ../paper.dat | python fixed_durations.py'

if __name__ == '__main__':
    reducer(sys.stdin)

