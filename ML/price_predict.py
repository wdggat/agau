#!/usr/bin/env python
#-*-coding: utf8 -*-

import sys 
import optimizations
import pydrawer

def reducer(lines, value_len):
    records = []
    domain = [(-100, 100)] * (value_len - 1) + [(-2000, 2000)]
    for line in lines:
        items = line.strip().split()
	items = [float(item) for item in items]
	if len(items) != value_len: continue
        records.append(items)
       
    for denominator in [5 * (i+1) for i in range(40)]:
        best_cost, ave_cost, best_resolve, j = sys.maxint, sys.maxint, None, 0
        while ave_cost > 1000 and j < 1000:
#            best_cost, best_resolve = optimizations.randomoptimize(domain, get_costf(records, denominator))
            best_cost, best_resolve = optimizations.hill_climb(domain, get_costf(records, denominator))
#            best_cost, best_resolve = optimizations.annealing(domain, get_costf(records, denominator))
#            best_cost, best_resolve = optimizations.genetic_optimize(domain, get_costf(records, denominator))
            ave_cost = float(best_cost) / len(records)
	    if ave_cost < 2000:
                print 'best_cost: %s, best_resolve: %s, best_ave_cost: %f' % (best_cost, best_resolve, ave_cost)
	    j += 1
	print ' ---------------- denominator: %d, best_resolve: %s, best_ave_cost: %f --------------- ' % (denominator, best_resolve, ave_cost)

def get_expected(record, resolve, denominator=100):
    return sum([record[i] * resolve[i] for i in range(len(resolve) - 1)]) / denominator + resolve[-1]

# record: v1,v2...vn,actual 
# resolve: a1,a2..an,constant
def get_costf(records, denominator):
    def costf(resolve):
        min_cost = sys.maxint
        results = []
        for record in records:
            expected = get_expected(record, resolve, denominator)
            actual = record[-1]
            results.append((expected, actual))
        return sum([pow(expected - actual, 2) for (expected, actual) in results])
    return costf

#reference: the index of the reference value for comparison
def examine(lines, resolve, reference):
    resolve, deltaes, references, actuals, expecteds = eval(resolve), [], [], [], []
    for line in lines:
        items = line.strip().split()
        record = [float(item) for item in items]
        expected = get_expected(record, resolve)
        actual = record[-1]
        deltaes.append(expected - actual)

	references.append(record[reference])
	expecteds.append(expected)
	actuals.append(actual)
    print 'LENGTH: %s, same: %s' % (len(references), float(sum([1 for i in range(len(references)) if (expecteds[i] - references[i]) * (actuals[i] - references[i]) > 0])) / len(references))
    x = range(len(references))
    #pydrawer.draw(x, references, 'k', x, actuals, 'r-', x, expecteds, 'bo')
    pydrawer.draw(deltaes, 'bo')

def examine_delta(lines, resolve):
    resolve, deltaes, compares = eval(resolve), [], []
    for line in lines:
        items = line.strip().split()
        record = [float(item) for item in items]
        expected = get_expected(record, resolve)
        actual = record[-1]
        deltaes.append(expected - actual)
	compares.append((expected, actual))
    print 'pares: %s, same: %s' % (compares, float(sum([1 for (expected, actual) in compares if expected * actual > 0])) / len(compares))
    pydrawer.draw(deltaes, 'bo')

def print_usage():
    print 'Usage:'
    print '\tpython price_predict.py <LENGTH>'
    print '\tpython price_predict.py examine <resolve>'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        reducer(sys.stdin, int(sys.argv[1]))
    elif len(sys.argv) == 4 and sys.argv[1] == 'examine':
        examine(sys.stdin, sys.argv[2], int(sys.argv[3]))
    elif len(sys.argv) == 3 and sys.argv[1] == 'examine_delta':
        examine_delta(sys.stdin, sys.argv[2])
    else:
        print_usage()

