#!/usr/bin/env python

import sys
import utils
from agau import Agau

def reducer(lines):
    am_begins,am_ends,pm_begins,pm_ends,night_begins,night_ends = {},{},{},{},{},{}
    days = set()
    for line in lines:
        agtd = Agau.get_from_agauline(line)
	days.add(agtd.day)
	if utils.at_bid_time(agtd.dt):
	    continue
	if utils.in_morning(agtd.dt):
	    if not am_begins.get(agtd.day):
	        am_begins[agtd.day] = agtd.price
	    am_ends[agtd.day] = agtd.price
	if utils.in_afternoon(agtd.dt):
	    if not pm_begins.get(agtd.day):
	        pm_begins[agtd.day] = agtd.price
	    pm_ends[agtd.day] = agtd.price
	if utils.at_night(agtd.dt):
	    if not night_begins.get(agtd.day):
	        night_begins[agtd.day] = agtd.price
	    night_ends[agtd.day] = agtd.price

    print '%s\t\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ('DAY', 'NIGHT^', 'NIGHT$', 'AM^', 'AM$', 'PM^', 'PM$', 'DIRE_SAME')
    for day in sorted(days):
        alter_same = '-'
	if (pm_ends.get(day, 0) - am_begins.get(day, 0)) * (night_ends.get(day, 0) - night_begins.get(day, 0)) > 0 or night_ends.get(day, 0) - night_begins.get(day, 0) == 0: 
	    alter_same = '+'
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (day, night_begins.get(day, 0), night_ends.get(day, 0), am_begins.get(day, 0), am_ends.get(day, 0), pm_begins.get(day, 0), pm_ends.get(day, 0), alter_same)

if __name__ == '__main__':
    reducer(sys.stdin)

