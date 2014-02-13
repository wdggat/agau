#!/usr/bin/python 

import sys
import utils

NIGHT_ONLY, ALL_DAY = 0, 1

#Ag(T+D)	4052.00	-0.58%	279976	4082.00	4063.00	4087.00	4045.00	2014-02-11 22:01:03
def reducer(max_type):
    max_prices, max_times, min_times, min_prices = {}, {}, {}, {}
    days = set()
    for line in sys.stdin:
        items = line.strip().split('\t')
	price, dt = float(items[1]), utils.get_datetime(items[-1])
	if utils.at_bid_time(dt):
	    continue
        if max_type == NIGHT_ONLY and not utils.at_night(dt):
	    continue

        day = utils.get_agau_day(dt)
        if price > max_prices.get(day, 0):
	    max_prices[day] = price 
	    max_times[day] = items[-1]
	if price < min_prices.get(day, sys.maxint):
	    min_prices[day] = price
	    min_times[day] = items[-1]
	days.add(day)

    print '%s\t\t%s\t%s\t\t%s\t%s\t\t%s' % ('DAY', 'MAX_PRICE', 'MAX_AT', 'MIN_PRICE', 'MIN_AT', 'DELTA')
#    print max_prices,max_times, min_prices, min_times
    for day in sorted(days):
        print '%s\t%s\t%s\t%s\t%s\t%s' % (day, max_prices[day], max_times[day], min_prices[day], min_times[day], max_prices[day] - min_prices[day])

def print_usage():
    print 'Usage:'
    print 'grep -e "Ag" ../agau.dat | python extrame_price_reducer.py (0|1)'

if __name__ == '__main__':
    max_type = ALL_DAY
    if len(sys.argv) > 1 and int(sys.argv[1]) == NIGHT_ONLY:
        max_type = NIGHT_ONLY
    reducer(max_type)

