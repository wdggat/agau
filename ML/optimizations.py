#!/usr/bin/env python

import sys
import random

def randomoptimize(domain, costf):
    best = sys.maxint
    best_resolve = None
    for i in range(1000000):
        resolve = [random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))]
	cost = costf(resolve)

	if cost < best:
	    best = cost 
	    best_resolve = resolve
#        print 'round: %d, cost: %s, resolve: %s' % (i, cost, resolve)
#    print 'BEST -- cost: %s, resolve: %s' % (best, best_resolve)
    return best,best_resolve

