#!/usr/bin/env python

import sys

#NO	DAY	--NIGHT^	NIGHT$-^	--AM^	AM^-$	--PM^	PM^-$
def reducer(lines):
    titles = '--NIGHT^        NIGHT$-^        --AM^   AM^-$   --PM^   PM^-$'.split()
    same, zero, diff = {}, {}, {}
    for line in lines:
        items = line.strip().split('\t')
	if len(items) != 8 or items[0] == 'NO': continue
        for i in range(len(titles) - 1):
	    for j in range(i + 1, len(titles)):
	        if items[i + 2] and items[j + 2]:
                    f1,f2 = float(items[i + 2]), float(items[j + 2])
	            key = (i, j)
                    if f1 * f2 > 0 or (f1 == 0 and f2 > 0):
		        same[key] = same.get(key, 0) + 1
		    if f1 * f2 < 0 or (f1 == 0 and f2 < 0):
		        diff[key] = diff.get(key, 0) + 1
		    if f2 == 0:
		        zero[key] = zero.get(key, 0) + 1

    for (i, j) in same.keys():
        print '(%s, %s): (%s, %s, %s)' % (titles[i], titles[j], same.get((i,j), 0), zero.get((i,j), 0), diff.get((i,j), 0))

def print_usage():
    print 'cat stage_alters.txt | python stage_diraction_relations.py'

if __name__ == '__main__':
    reducer(sys.stdin)

