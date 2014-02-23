#!/usr/bin/env python

import sys

#NO	DAY	--NIGHT^	NIGHT$-^	--AM^	AM^-$	--PM^	PM^-$
def reducer(lines):
    for threshold in range(50):
        same, zero, diff = {}, {}, {}
        for line in lines:
            items = line.strip().split('\t')
    	    if len(items) != DATA_LEN or items[0] == 'NO': continue
            for i in range(len(titles) - 1):
    	        for j in range(i + 1, len(titles)):
    	            if items[i + SHIFT] and items[j + SHIFT]:
                        f1,f2 = float(items[i + SHIFT]), float(items[j + SHIFT])

                        if abs(f1) < threshold:
			    continue

    	                key = (i, j)
                        if f1 * f2 > 0 or (f1 == 0 and f2 > 0):
    		            same[key] = same.get(key, 0) + 1
    		        if f1 * f2 < 0 or (f1 == 0 and f2 < 0):
    		            diff[key] = diff.get(key, 0) + 1
    		        if f2 == 0:
    		            zero[key] = zero.get(key, 0) + 1
    
        for (i, j) in same.keys():
#            print '(%s, %s): (%s, %s, %s)' % (titles[i], titles[j], same.get((i,j), 0), zero.get((i,j), 0), diff.get((i,j), 0))
            sumdays = same.get((i,j), 0) + zero.get((i,j), 0) + diff.get((i,j), 0)
	    if sumdays < RECORD_LIMIT:
	        continue
	    if float(same.get((i,j), 0)) / sumdays > ODD or float(diff.get((i,j), 0)) / sumdays > ODD:
                print '%s\t(%s, %s): (%s, %s, %s)' % (threshold, titles[i], titles[j], same.get((i,j), 0), zero.get((i,j), 0), diff.get((i,j), 0))

def print_usage():
    print 'cat stage_alters.ag | python stage_threshold_odds.py (day|night)'

if __name__ == '__main__':
    if sys.argv[1] == 'day':
        titles = '--NIGHT^        NIGHT$-^        --AM^   AM^-$   --PM^   PM^-$'.split()
        DATA_LEN = 8
	SHIFT = 2
	ODD = 0.75
	RECORD_LIMIT = 10
    elif sys.argv[1] == 'night':
        titles = '20        21        22   23   00   01	02'.split()
        DATA_LEN = 8
	SHIFT = 1
	ODD = 0.75
	RECORD_LIMIT = 5
    lines = [line for line in sys.stdin]
    reducer(lines)

