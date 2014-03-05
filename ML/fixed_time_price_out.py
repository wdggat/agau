
#!/usr/bin/env python

import sys
sys.path.append('../etl/')
from agau import Agau 
from datetime import datetime
from datetime import timedelta
import utils

# last_closed, open_price, 21:00, 21:10, 21:20, 21:30, 21:40, 21:50, 22:00, closed_price
def get_dts1():
    td = timedelta(minutes=10)
    dt_begin = datetime(1970,1,1,21,0,0)
    return [dt_begin, dt_begin + td, dt_begin + td * 2, dt_begin + td * 3, dt_begin + td * 4, dt_begin + td * 5, dt_begin + td * 6]

# last_closed, open_price, 21:00, 21:30, 22:00, 22:30, 23:00, closed_price
def get_dts2():
    td = timedelta(minutes=30)
    dt_begin = datetime(1970,1,1,21,0,0)
    return [dt_begin, dt_begin + td, dt_begin + td * 2, dt_begin + td * 3, dt_begin + td * 4]

def reducer(lines):
    dts = get_dts2()
    prices = [None] * len(dts)
    pre_day, day, out_str = None, None, None
    for line in lines:
        ag = Agau.get_from_agauline(line)
	day = ag.day
	if not pre_day: pre_day = day
	if day != pre_day and not (ag.dt.weekday() == 0 and ag.dt.hour < 21):
	    if out_str:
	        print '%s\t%s' % (out_str, ag.closed_price)
	    prices = [None] * len(dts)
	    out_str = None
	    pre_day = day
	for i in range(len(dts)):
	    if utils.is_dt_nearby(ag.dt, dts[i].hour, dts[i].minute):
                prices[i] = ag.price
                if i == len(dts) - 1:
		    if all(prices):
		        out_str = '%s\t%s\t%s' % (ag.closed_price, ag.open_price, '\t'.join([str(p) for p in prices]))
	            prices = [None] * len(dts)

def print_usage():
    print 'Usage:'
    print 'grep -e "Ag" ../agau.dat | python fixed_time_price_out.py'

if __name__ == '__main__':
    reducer(sys.stdin)

