#!/usr/bin/env python
#-*-coding: utf8 -*-

import sys
sys.path.append('../etl/')
from history import History
import optimizations
import pydrawer

#GOAL: < 26200, 100 daily
def random_reducer(lines):
    # 开盘价, 昨结算, 最高价, 最低价, 加权平均价, 成交量（千克）持仓量 
#    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    records = set()
    for line in lines:
        history_record = History.get_from_historyline(line)
	history_record = History.norm(history_record)
	records.add(history_record)

    best_cost,best_resolve = sys.maxint, None
    for i in range(20):
        cost, resolve = optimizations.randomoptimize(domain, get_best_solution(records))
#        cost, resolve = optimizations.hill_climb(domain, get_best_solution(records))
        print 'i: %s, cost: %s, resolve: %s, ave_cost: %f' % (i, cost, resolve, cost / len(records))
	if cost < best_cost:
	    best_cost = cost 
	    best_resolve = resolve
	# goal: daily_cost <= sqrt(100)
	if best_cost <= len(records) * 100:
	    break
    print 'best_cost: %s, best_resolve: %s, best_ave_cost: %f' % (best_cost, best_resolve, best_cost / len(records))

def get_expected(resolve, record):
#    return (record.open_price * resolve[0] + record.closed_price * resolve[1] + record.high * resolve[2] + record.low * resolve[3] + record.average * resolve[4] + record.dealed_num * resolve[5] + record.hold * resolve[6]) / 100 + resolve[-1]
    return (record.open_price * resolve[0] + record.closed_price * resolve[1] + record.high * resolve[2] + record.low * resolve[3]) / 100 + resolve[-1]

def get_best_solution(records):
    def costf(resolve):
        actuals = {}
        for record in records:
	    expected = get_expected(resolve, record)
	    actual = record.closed_today 
	    actuals[actual] = expected
	return sum([pow(actual - actuals[actual], 2) for actual in actuals.keys()])
    return costf

def examine(lines, pic_kind):
    resolve = [-36, -5, 97, 44, -24]
    length, same, deltaes,days,opens,actuals,expecteds = 0, 0, [],[],[],[],[]
    for line in lines:
        record = History.get_from_historyline(line)
	record = History.norm(record)
	expected = get_expected(resolve, record)
	actual = record.closed_today 
	delta = expected - actual
	deltaes.append(delta)
	days.append(record.day)
	opens.append(record.open_price)
	actuals.append(actual)
	expecteds.append(expected)
	print 'open: %s,actual: %s, expected: %s, delta: %s' % (record.open_price, actual, expected, delta)

	if (expected - record.open_price) * (actual - record.open_price) > 0:
	    same += 1
	length += 1
    print 'direction_same: %d, length: %d, direction_same/length: %s' % (same, length, float(same)/length)
    x = [ i + 1 for i in range(len(opens))]
    if pic_kind == 'delta':
        pydrawer.draw(x, deltaes, 'bo')
    if pic_kind == 'lines':
        pydrawer.draw(x, opens,'k', x, actuals,'r-', x, expecteds,'bo')

def hill_climb_reducer(lines):
    # 开盘价, 昨结算, 最高价, 最低价
    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    records = set()
    for line in lines:
        history_record = History.get_from_historyline(line)
	history_record = History.norm(history_record)
	records.add(history_record)

    while(True):
        best_cost, best_resolve = optimizations.hill_climb(domain, get_best_solution(records))
	ave_cost = best_cost / len(records)
	if ave_cost < 3000:
            print 'best_cost: %s, best_resolve: %s, best_ave_cost: %f' % (best_cost, best_resolve, ave_cost)
	    if ave_cost < 1000:
	        break

def anneal_reducer(lines):
    # 开盘价, 昨结算, 最高价, 最低价
    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    records = set()
    for line in lines:
        history_record = History.get_from_historyline(line)
	history_record = History.norm(history_record)
	records.add(history_record)

    while(True):
        best_cost, best_resolve = optimizations.annealing(domain, get_best_solution(records))
	ave_cost = best_cost / len(records)
	if ave_cost < 3000:
            print 'best_cost: %s, best_resolve: %s, best_ave_cost: %f' % (best_cost, best_resolve, ave_cost)
	    if ave_cost < 1000:
	        break

def genetic_reducer(lines):
    # 开盘价, 昨结算, 最高价, 最低价
    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    records = set()
    for line in lines:
        history_record = History.get_from_historyline(line)
	history_record = History.norm(history_record)
	records.add(history_record)

    while(True):
        best_cost, best_resolve = optimizations.genetic_optimize(domain, get_best_solution(records))
	ave_cost = best_cost / len(records)
	if ave_cost < 3000:
            print 'best_cost: %s, best_resolve: %s, best_ave_cost: %f' % (best_cost, best_resolve, ave_cost)
	    if ave_cost < 1000:
	        break

def print_usage():
    print 'Usage:'
    print '\t./ag_au_price_predict.py (random|hill_climb|anneal|genetic)'
    print '\t./ag_au_price_predict.py examine (lines|delta)'

if __name__ == '__main__':
    if sys.argv[1] == 'random':
        random_reducer(sys.stdin)
    elif sys.argv[1] == 'hill_climb':
        hill_climb_reducer(sys.stdin)
    elif sys.argv[1] == 'anneal':
        anneal_reducer(sys.stdin)
    elif sys.argv[1] == 'genetic':
        genetic_reducer(sys.stdin)
    elif sys.argv[1] == 'examine' and sys.argv[2] in ('lines', 'delta'):
        examine(sys.stdin, sys.argv[2])
    else:
        print_usage()

