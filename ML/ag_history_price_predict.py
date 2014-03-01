#!/usr/bin/env python
#-*-coding: utf8 -*-

import sys
sys.path.append('../etl/')
from history import History
import optimizations

#GOAL: < 26200, 100 daily
def reducer(lines):
    # 开盘价, 昨结算, 最高价, 最低价, 加权平均价, 成交量（千克） 成交金额（元） 持仓量 交收方向
    domain = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-2000, 2000)]
    records = set()
    for line in lines:
        history_record = History.get_from_historyline(line)
	history_record = norm(history_record)
	records.add(history_record)

    best_cost,best_resolve = sys.maxint, None
    for i in range(10):
        cost, resolve = optimizations.randomoptimize(domain, get_best_solution(records))
        print 'i: %s, cost: %s, resolve: %s' % (i, cost, resolve)
	if cost < best_cost:
	    best_cost = cost 
	    best_resolve = resolve
	if best_cost <= len(records) * 100:
	    break
    print 'best_cost: %s, best_resolve: %s' % (best_cost, best_resolve)

def norm(history_record):
    history_record.hold /= 10 
    history_record.dealed_num /= 10
    history_record.dealed_money /= 10000 
    if history_record.pay_direction == '多支付空':
        history_record.pay_direction = 1
    else:
        history_record.pay_direction = -1
    return history_record

def get_best_solution(records):
    def costf(resolve):
        actuals = {}
        for record in records:
	    expected = (record.open_price * resolve[0] + record.closed_price * resolve[1] + record.high * resolve[2] + record.low * resolve[3] + record.average * resolve[4] + record.dealed_num * resolve[5] + record.dealed_money * resolve[6] + record.hold * resolve[7]) / 100 + resolve[-1]
	    actual = record.closed_today 
	    actuals[actual] = expected
	return sum([pow(actual - actuals[actual], 2) for actual in actuals.keys()])
    return costf

def examine(lines):
    resolve = [58, -55, 66, -77, -84, 18, -16, 12, -1, -722569]
    for line in lines:
        record = History.get_from_historyline(line)
	record = norm(record)
	expected = record.open_price * resolve[0] + record.closed_price * resolve[1] + record.high * resolve[2] + record.low * resolve[3] + record.average * resolve[4] + record.dealed_num * resolve[5] + record.dealed_money * resolve[6] + record.hold * resolve[7]  + record.pay_direction * resolve[8] + resolve[-1]
	actual = record.closed_today * 100
	print 'actual: %s, expected: %s' % (actual, expected)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        reducer(sys.stdin)
    if len(sys.argv) == 2 and sys.argv[1] == 'examine':
        examine(sys.stdin)
