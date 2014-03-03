#!/usr/bin/env python
#-*-coding: utf8 -*-

import sys
sys.path.append('../etl/')
from history import History
import optimizations

#GOAL: < 26200, 100 daily
def random_reducer(lines):
    # 开盘价, 昨结算, 最高价, 最低价, 加权平均价, 成交量（千克）持仓量 
#    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    records = set()
    for line in lines:
        history_record = History.get_from_historyline(line)
	history_record = norm(history_record)
	records.add(history_record)

    best_cost,best_resolve = sys.maxint, None
    for i in range(200):
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

def norm(history_record):
    history_record.hold /= 10 
    history_record.dealed_num /= 10
#    if history_record.pay_direction == '多支付空':
#        history_record.pay_direction = 1
#    else:
#        history_record.pay_direction = -1
    return history_record

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

def examine(lines):
    resolve = [58, -55, 66, -77, -84, 18, -16, -1, -722569]
    for line in lines:
        record = History.get_from_historyline(line)
	record = norm(record)
	expected = get_expected(resolve, record)
	actual = record.closed_today * 100
	print 'actual: %s, expected: %s' % (actual, expected)

def hill_climb_reducer(lines):
    # 开盘价, 昨结算, 最高价, 最低价
    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    records = set()
    for line in lines:
        history_record = History.get_from_historyline(line)
	history_record = norm(history_record)
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
	history_record = norm(history_record)
	records.add(history_record)

    while(True):
        best_cost, best_resolve = optimizations.annealing(domain, get_best_solution(records))
	ave_cost = best_cost / len(records)
	if ave_cost < 3000:
            print 'best_cost: %s, best_resolve: %s, best_ave_cost: %f' % (best_cost, best_resolve, ave_cost)
	    if ave_cost < 1000:
	        break

if __name__ == '__main__':
    if sys.argv[1] == 'random':
        random_reducer(sys.stdin)
    elif sys.argv[1] == 'hill_climb':
        hill_climb_reducer(sys.stdin)
    elif sys.argv[1] == 'anneal':
        anneal_reducer(sys.stdin)
    elif sys.argv[1] == 'examine':
        examine(sys.stdin)
    else:
        print_usage()

