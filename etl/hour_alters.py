#!/usr/bin/python 

import sys
import utils
from agau import Agau

def reducer(lines):
    print 'DAY\t\t20:50\t21:00\t22:00\t23:00\t0:00\t1:00\t2:00'
    bids,ends,begins = {},{},{}
    for line in lines:
        ag = Agau.get_from_agauline(line)
	bids[ag.day] = ag.price - ag.closed_price
	if not utils.at_night(ag.dt):
	    continue
        ends.setdefault(ag.day, {})
	ends[ag.day][ag.dt.hour] = ag.price
        begins.setdefault(ag.day, {})
        if begins[ag.day].get(ag.dt.hour) in (None, 0):
	    begins[ag.day][ag.dt.hour] = ag.price

    for day in sorted(ends.keys()):
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (day, bids[day], ends[day].get(21, 0) - begins[day].get(21, 0), ends[day].get(22, 0) - begins[day].get(22, 0), ends[day].get(23, 0) - begins[day].get(23, 0), ends[day].get(0, 0) - begins[day].get(0, 0), ends[day].get(1, 0) - begins[day].get(1, 0), ends[day].get(2, 0) - begins[day].get(2, 0))

def print_usage():
    print 'Usage:'
    print 'grep -e "Ag" ../agau.dat | python hour_alters.py > hour_alters.ag'

if __name__ == '__main__':
    reducer(sys.stdin)

