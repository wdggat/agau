#!/usr/bin/env python

import sys
import utils
from agau import Agau
from datetime import datetime

lim_hour, lim_minute = 23, 0

def reducer(lines):
    timestamps = {}
    for line in lines:
        agtd = Agau.get_from_agauline(line)
	natual_day = agtd.dt.strftime('%Y-%m-%d')
	if (not utils.at_night(agtd.dt)) or ((natual_day == agtd.day and agtd.dt.hour < lim_hour) or (agtd.dt.hour == lim_hour and agtd.dt.minute < lim_minute)) or timestamps.get(agtd.day, '-').startswith('2'):
#	    print 'PASS: %s' % agtd.time
	    continue
        if agtd.price > agtd.open_price:
	    if timestamps.get(agtd.day) == '-':
	        timestamps[agtd.day] = agtd.time 
            else:
	        timestamps[agtd.day] = '+'
        elif agtd.price < agtd.open_price:
	    if timestamps.get(agtd.day) == '+':
	        timestamps[agtd.day] = agtd.time 
            else:
	        timestamps[agtd.day] = '-'
        elif agtd.price == agtd.open_price:
            timestamps[agtd.day] = agtd.time

    i = 1
    print '%s\t%s\t\t%s\t%s' % ('NO', 'DAY', 'TIMESTAMP', 'DELTA')
    for day in sorted(timestamps.keys()):
        print '%s\t%s\t%s' % (i, day, timestamps.get(day))
	i += 1

def print_usage():
    print 'grep -e "Ag" ../agau.dat | python backto_open_reducer.py'

if __name__ == '__main__':
    reducer(sys.stdin)

