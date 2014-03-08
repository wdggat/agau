#!/usr/bin/env python
#-*-coding: utf8 -*-

import sys 
import optimizations
import pydrawer

def reducer(lines, value_len):
    reference, records = 1, []
    domain = [(-100, 100)] * (value_len - 1) + [(-2000, 2000)]
    for line in lines:
        items = line.strip().split()
	items = [float(item) for item in items]
	if len(items) != value_len: continue
        records.append(items)
       
    best_denominator,best_ave_cost, best_resolve, LENGTH, best_SAME = 0, sys.maxint, None, 0, 0
    for denominator in [5 * (i+1) for i in range(40)]:
        j = 0
        while j < 1000:
#            best_cost, best_resolve = optimizations.randomoptimize(domain, get_costf(records, denominator))
            cost, resolve = optimizations.hill_climb(domain, get_costf(records, denominator))
	    LENGTH, SAME = examine(records, resolve, reference, denominator, False)
#            best_cost, best_resolve = optimizations.annealing(domain, get_costf(records, denominator))
#            best_cost, best_resolve = optimizations.genetic_optimize(domain, get_costf(records, denominator))
            ave_cost = float(cost) / len(records)
	    if ave_cost < 2000 or SAME > 0.85 or SAME < 0.15:
                print 'best_resolve: %s, best_ave_cost: %f, LENGTH: %d, SAME: %f' % (resolve, ave_cost, LENGTH, SAME)
	    if best_ave_cost > ave_cost:
	        best_ave_cost = ave_cost
		best_resolve = resolve
		best_denominator = denominator
		best_SAME = SAME
	    j += 1
	print ' ---------------- denominator: %d, best_denominator: %d, best_resolve: %s, best_ave_cost: %f, LENGTH: %d, SAME: %f --------------- ' % (denominator, best_denominator, best_resolve, best_ave_cost, LENGTH, best_SAME)

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
def examine(records, resolve, reference, denominator=100, show=True):
    deltaes, references, actuals, expecteds = [], [], [], []
    for record in records:
        expected = get_expected(record, resolve, denominator)
        actual = record[-1]
        deltaes.append(expected - actual)

	references.append(record[reference])
	expecteds.append(expected)
	actuals.append(actual)
    LENGTH, SAME = len(references), float(sum([1 for i in range(len(references)) if (expecteds[i] - references[i]) * (actuals[i] - references[i]) > 0])) / len(references)
    print 'LENGTH: %s, same: %s' % (LENGTH, SAME)
    if show:
        x = range(len(deltaes))
        pydrawer.draw(x, references, 'k', x, actuals, 'r-', x, expecteds, 'bo')
        #pydrawer.draw(deltaes, 'bo')
    return LENGTH, SAME

def examine_reducer(lines, resolve, reference, denominator=100):
    records = []
    for line in lines:
        items = line.strip().split()
        record = [float(item) for item in items]
	records.append(record)
    examine(records, eval(resolve), reference, denominator)

# delta seems to be useless
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
    print '\tpython price_predict.py examine <resolve> reference_index denominator'
    print '\tpython price_predict.py examine_delta <resolve>'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        reducer(sys.stdin, int(sys.argv[1]))
    elif len(sys.argv) == 5 and sys.argv[1] == 'examine':
        examine_reducer(sys.stdin, sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif len(sys.argv) == 3 and sys.argv[1] == 'examine_delta':
        examine_delta(sys.stdin, sys.argv[2])
    else:
        print_usage()

