#!/usr/bin/env python
#-*-coding: utf8 -*-

import sys 
import optimizations
import pydrawer
from solution import Solution
from adjuster import Adjuster

def reducer(lines, adjuster):
    records = []
    for line in lines:
        items = line.strip().split()
	items = [float(item) for item in items]
	if len(items) != adjuster.value_len: continue
        records.append(items)
       
    best_sol = Solution.EMPTY()
    for denominator in adjuster.denominators:
        j = 0
        while j < 100:
#            best_cost, best_resolve = optimizations.randomoptimize(domain, get_costf(records, denominator))
            cost, resolve = optimizations.hill_climb(domain, get_costf(records, denominator))
	    LENGTH, SAME = examine(records, resolve, adjuster.reference, denominator, False)
#            best_cost, best_resolve = optimizations.annealing(domain, get_costf(records, denominator))
#            best_cost, best_resolve = optimizations.genetic_optimize(domain, get_costf(records, denominator))
            ave_cost = float(cost) / len(records)
	    sol = Solution(denominator, resolve, ave_cost, LENGTH, SAME)
	    if sol.ave_cost < adjuster.ave_cost_need or sol.SAME > 0.80 or sol.SAME < 0.20:
                #print 'best_resolve: %s, best_ave_cost: %f, LENGTH: %d, SAME: %f' % (resolve, ave_cost, LENGTH, SAME)
		print 'Solution found: %s' % sol
	    if best_sol.ave_cost > sol.ave_cost:
	        best_sol = sol
	    j += 1
	print ' ---------------- denominator: %d, {%s} --------------- ' % (denominator, best_sol)
    return best_sol

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

def examine(records, resolve, reference, denominator=100, show=True):
    deltaes, references, actuals, expecteds = [], [], [], []
    for record in records:
        expected = get_expected(record, resolve, denominator)
        actual = record[-1]
        deltaes.append(expected - actual)
        if reference != -1:
	    references.append(record[reference])
	else:
	    references.append(0)
	expecteds.append(expected)
	actuals.append(actual)
    LENGTH, SAME = len(references), float(sum([1 for i in range(len(references)) if (expecteds[i] - references[i]) * (actuals[i] - references[i]) > 0])) / len(references)
    #print 'LENGTH: %s, same: %s' % (LENGTH, SAME)
    if show:
        x = range(len(deltaes))
        #pydrawer.draw(x, references, 'k', x, actuals, 'r-', x, expecteds, 'bo')
        pydrawer.draw(deltaes, 'bo')
    return LENGTH, SAME

def examine_reducer(lines, resolve, reference, denominator=100):
    records = []
    for line in lines:
        items = line.strip().split()
        record = [float(item) for item in items]
	records.append(record)
    examine(records, eval(resolve), reference, denominator)

def print_usage():
    print 'Usage:'
    print '\tpython price_predict.py ADJUSTER'
    print '\tpython price_predict.py examine <resolve> reference_index denominator'
    print '\tpython price_predict.py examine_delta <resolve>'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        reducer(sys.stdin, adjuster.get_adjuster(sys.argv[1]))
    elif len(sys.argv) == 5 and sys.argv[1] == 'examine':
        examine_reducer(sys.stdin, sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif len(sys.argv) == 3 and sys.argv[1] == 'examine_delta':
        examine_delta(sys.stdin, sys.argv[2])
    else:
        print_usage()

