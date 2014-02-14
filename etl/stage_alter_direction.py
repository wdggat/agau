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

    print '%s\t%s\t\t%s\t%s\t%s\t%s\t%s' % ('NO', 'DAY', 'NIGHT$-^', '--AM^', 'AM^-$', '--PM^', 'PM^-$')
    i = 0
    for day in sorted(days):
        a,b,c,d,e = None,None,None,None,None 
	i += 1
	a = night_ends.get(day, 0) - night_begins.get(day, 0)
	b = am_begins.get(day, 0) - night_ends.get(day, 0)
	c = am_ends.get(day, 0) - am_begins.get(day, 0)
	d = pm_begins.get(day, 0) - am_ends.get(day, 0)
	e = pm_ends.get(day, 0) - pm_begins.get(day, 0)
#	if night_ends.get(day, 0) - night_begins.get(day, 0) > 0:
#	    a = '+'
#	elif night_ends.get(day, 0) - night_begins.get(day, 0) < 0:
#	    a = '-'
#	elif night_ends.get(day, 0) - night_begins.get(day, 0) == 0:
#	    a = '='
#	if am_begins.get(day, 0) - night_ends.get(day, 0) > 0:
#	    b = '+'
#	elif am_begins.get(day, 0) - night_ends.get(day, 0) < 0:
#	    b = '-'
#	elif am_begins.get(day, 0) - night_ends.get(day, 0) == 0:
#	    b = '='
#	if am_ends.get(day, 0) - am_begins.get(day, 0) > 0:
#	    c = '+'
#	elif am_ends.get(day, 0) - am_begins.get(day, 0) < 0:
#	    c = '-'
#	elif am_ends.get(day, 0) - am_begins.get(day, 0) == 0:
#	    c = '='
#	if pm_begins.get(day, 0) - am_ends.get(day, 0) > 0:
#	    d = '+'
#	elif pm_begins.get(day, 0) - am_ends.get(day, 0) < 0:
#	    d = '-'
#	elif pm_begins.get(day, 0) - am_ends.get(day, 0) == 0:
#	    d = '='
#	if pm_ends.get(day, 0) - pm_begins.get(day, 0) > 0:
#	    e = '+'
#	elif pm_ends.get(day, 0) - pm_begins.get(day, 0) < 0:
#	    e = '-'
#	elif pm_ends.get(day, 0) - pm_begins.get(day, 0) == 0:
#	    e = '='
	print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (i, day, a,b,c,d,e)

def print_usage():
    print 'Usage:'
    print '\tgrep -e "Ag" ../agau.dat | python stage_alter_direction_reducer.py'

if __name__ == '__main__':
    reducer(sys.stdin)
  
