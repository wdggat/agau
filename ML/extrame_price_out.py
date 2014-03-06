#!/usr/bin/python 

import sys
sys.path.append('../etl/')
from agau import Agau

# last_closed, open_price, high in 21, low in 21, 22:00, close_today
def reducer(lines):
    high, low = 0, sys.maxint
    pre_day, day, out_str = None, None, None
    for line in lines:
        ag = Agau.get_from_agauline(line)
	day = ag.day
	if not pre_day: pre_day = day
	if day != pre_day and not (ag.dt.weekday() == 0 and ag.dt.hour < 21):
	    if out_str:
	        print '%s\t%s' % (out_str, ag.closed_price)
	    high, low = 0, sys.maxint
	    out_str = None
	    pre_day = day
        
	if ag.dt.hour == 21:
	    if ag.price > high:
	        high = ag.price
	    if ag.price < low:
	        low = ag.price
	if ag.dt.hour == 22 and not out_str:
	    #out_str = '%s\t%s\t%s\t%s\t%s' % (ag.closed_price, ag.open_price, high, low, ag.price)
	    out_str = '%s\t%s\t%s\t%s' % (ag.closed_price, ag.open_price, high, low)

def reducer_delta(lines):
    high, low, closed_price = 0, sys.maxint, sys.maxint
    pre_day, day, out_str = None, None, None
    for line in lines:
        ag = Agau.get_from_agauline(line)
	day = ag.day
	if not pre_day: pre_day = day
	if day != pre_day and not (ag.dt.weekday() == 0 and ag.dt.hour < 21):
	    if out_str:
	        print '%s\t%s' % (out_str, ag.closed_price - closed_price)
	    high, low,closed_price = 0, sys.maxint,sys.maxint
	    out_str = None
	    pre_day = day
        
	if ag.dt.hour == 21:
	    if ag.price > high:
	        high = ag.price
	    if ag.price < low:
	        low = ag.price
	if ag.dt.hour == 22 and not out_str:
	    #out_str = '%s\t%s\t%s\t%s' % (ag.open_price - ag.closed_price,  high - ag.closed_price, low - ag.closed_price, ag.price - ag.closed_price)
	    out_str = '%s\t%s\t%s' % (ag.open_price - ag.closed_price,  high - ag.closed_price, low - ag.closed_price)
	    closed_price = ag.closed_price

if __name__ == '__main__':
    reducer_delta(sys.stdin)

