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

    days,deleted = sorted(days),[]
    if len(sys.argv) == 2 and sys.argv[1] == '--fix':
        for i in range(len(days) - 1):
	    day, next_day = days[i], days[i + 1]
	    if am_begins.get(day) == None and am_ends.get(day) == None and pm_begins.get(day) == None and pm_ends.get(day) == None and night_begins.get(next_day) == None and night_ends.get(next_day) == None:
	        am_begins[day] = am_begins[next_day]
		am_ends[day] = am_ends[next_day]
                pm_begins[day] = pm_begins[next_day]
		pm_ends[day] = pm_ends[next_day]
		deleted.append(next_day)

    for day in deleted:
        days.remove(day)

    print '%s\t%s\t\t%s\t%s\t%s\t%s\t%s\t%s' % ('NO', 'DAY', 'NIGHT^', 'NIGHT$', 'AM^', 'AM$', 'PM^', 'PM$')
    i = 0
    for day in days:
        i += 1
	print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (i, day, night_begins.get(day, 0), night_ends.get(day, 0), am_begins.get(day, 0), am_ends.get(day, 0), pm_begins.get(day, 0), pm_ends.get(day, 0))

def print_usage():
    print 'Usage:'
    print '\tgrep -e "Ag" ../agau.dat | python boundary_prices.py <--fix>'

if __name__ == '__main__':
    reducer(sys.stdin)
  
