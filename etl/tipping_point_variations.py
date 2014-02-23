#!/usr/bin/env python

import sys
import utils
from agau import Agau

def reducer(lines):
    begins, extremums = {},{}
    print 'DAY\t\tDELTA'
    for line in lines:
        agtd = Agau.get_from_agauline(line)
	if agtd.dt.hour == 21 and agtd.dt.minute in (28,29,30,31,32,33,34):
	    day = agtd.day
	    if begins.get(day) == None and agtd.dt.minute in (28, 29):
	        begins[day] = agtd.price 
	    if abs(extremums.get(day, begins[day]) - begins[day]) <= abs(agtd.price - begins[day]):
	        extremums[day] = agtd.price 

    for day in sorted(begins.keys()):
        print '%s\t%s' % (day, extremums[day] - begins[day])

def print_usage():
    print 'grep -e "Ag" ../agau.dat | python tipping_point_variations.py > tipping_points.ag'

if __name__ == '__main__':
    reducer(sys.stdin)
