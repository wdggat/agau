#!/usr/bin/env python

import sys
sys.path.append('../etl/')
from agau import Agau 
from datetime import datetime
from datetime import timedelta
import utils

def reducer(lines):
    td = timedelta(minutes=5)
    dt_begin = datetime(1970,1,1,21,0,0)
    dt_5 = dt_begin + td
    dt_10 = dt_5 + td
    dt_15 = dt_10 + td
    dt_20 = dt_15 + td
    dt_30 = dt_20 + td * 2
    price_0, price_5, price_10, price_15, price_20, price_30 = None, None, None, None, None, None
    for line in lines:
        ag = Agau.get_from_agauline(line)        
        if utils.is_dt_nearby(ag.dt, dt_begin.hour, dt_begin.minute):
	    price_0 = ag.price
        elif utils.is_dt_nearby(ag.dt, dt_5.hour, dt_5.minute):
	    price_5 = ag.price
        elif utils.is_dt_nearby(ag.dt, dt_10.hour, dt_10.minute):
	    price_10 = ag.price
        elif utils.is_dt_nearby(ag.dt, dt_15.hour, dt_15.minute):
	    price_15 = ag.price
        elif utils.is_dt_nearby(ag.dt, dt_20.hour, dt_20.minute):
	    price_20 = ag.price
        elif utils.is_dt_nearby(ag.dt, dt_30.hour, dt_30.minute):
	    price_30 = ag.price
	    if price_0 and price_5 and price_10 and price_15 and price_20 and price_30:
	        print '%s\t%s\t%s\t%s\t%s\t%s' % (price_0, price_5, price_10, price_15, price_20, price_30)
	    price_0, price_5, price_10, price_15, price_20, price_30 = None, None, None, None, None, None
	else:
	    continue

def print_usage():
    print 'Usage:'
    print 'grep -e "Ag" ../agau.dat | python duration_price_out.py'

if __name__ == '__main__':
    reducer(sys.stdin)

