#!/usr/bin/env python
#-*-coding: utf8 -*-

import sys 
import optimizations
import pydrawer

records = []
def reducer(lines, value_len):
    domain = [(-100, 100)] * (value_len - 1) + [(-2000, 2000)]
    for line in lines:
        items = line.strip().split()
	items = [float(item) for item in items]
	if len(items) != value_len: continue
        records.append(items)
        
    best_cost, ave_cost, best_resolve = sys.maxint, sys.maxint, None 
    while ave_cost > 1000:
#        best_cost, best_resolve = optimizations.randomoptimize(domain, costf)
#        best_cost, best_resolve = optimizations.hill_climb(domain, costf)
#        best_cost, best_resolve = optimizations.annealing(domain, costf)
        best_cost, best_resolve = optimizations.genetic_optimize(domain, costf)
        ave_cost = float(best_cost) / len(records)
        print 'best_cost: %s, best_resolve: %s, best_ave_cost: %f' % (best_cost, best_resolve, ave_cost)

def get_expected(record, resolve):
    return sum([record[i] * resolve[i] for i in range(len(resolve) - 1)]) + resolve[-1]

# record: v1,v2...vn,actual 
# resolve: a1,a2..an,constant
def costf(resolve):
    results = []
    for record in records:
        expected = get_expected(record, resolve)
	actual = record[-1]
        results.append((expected, actual))
    return sum([pow(expected - actual, 2) for (expected, actual) in results])

def examine(lines, resolve):
    resolve, deltaes = eval(resolve), []
    for line in lines:
        items = line.strip().split()
        record = [float(item) for item in items]
        expected = get_expected(record, resolve)
        actual = record[-1]
        deltaes.append(expected - actual)
    pydrawer.draw(deltaes, 'bo')

def print_usage():
    print 'Usage:'
    print '\tpython price_predict.py <LENGTH>'
    print '\tpython price_predict.py examine <resolve>'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        reducer(sys.stdin, int(sys.argv[1]))
    elif len(sys.argv) == 3 and sys.argv[1] == 'examine':
        examine(sys.stdin, sys.argv[2])
    else:
        print_usage()

