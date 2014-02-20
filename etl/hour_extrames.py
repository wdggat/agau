#!/usr/bin/python 

import sys
import utils
from agau import Agau

def reducer(lines):
    print 'DAY\t\t20:50\t21:00\t22:00\t23:00\t0:00\t1:00\t2:00'
    bids,maxs,mins = {},{},{}
    for line in lines:
        ag = Agau.get_from_agauline(line)
	bids[ag.day] = ag.price - ag.closed_price
	if not utils.at_night(ag.dt):
	    continue
        maxs.setdefault(ag.day, {})
        if ag.price > maxs[ag.day].get(ag.dt.hour, 0):
	    maxs[ag.day][ag.dt.hour] = ag.price
        mins.setdefault(ag.day, {})
        if ag.price < mins[ag.day].get(ag.dt.hour, sys.maxint):
	    mins[ag.day][ag.dt.hour] = ag.price

    for day in sorted(maxs.keys()):
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (day, bids[day], maxs[day].get(21, 0) - mins[day].get(21, 0), maxs[day].get(22, 0) - mins[day].get(22, 0), maxs[day].get(23, 0) - mins[day].get(23, 0), maxs[day].get(0, 0) - mins[day].get(0, 0), maxs[day].get(1, 0) - mins[day].get(1, 0), maxs[day].get(2, 0) - mins[day].get(2, 0))

def print_usage():
    print 'Usage:'
    print 'grep -e "Ag" ../agau.dat | python hour_extrames.py > hour_extrames.ag'

if __name__ == '__main__':
    reducer(sys.stdin)

