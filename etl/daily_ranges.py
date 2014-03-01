#!/usr/bin/env python
#-*-coding: utf-8 -*-

import sys
from history import History
import utils

#交易品种 日期 开盘价 最新价 昨结算 最高价 最低价 收盘价 涨跌（元） 涨跌幅 加权平均价 成交量（千克） 成交金额（元） 持仓量 交收方向
def reducer(lines, ABS):
#    print '[0, 3000), [3000, 4000), [4000, 5000), [5000, 6000), [6000,sys.maxint) '
    rates = {}
    for line in lines:
        history_ag = History.get_from_historyline(line)
        if history_ag.average < 3000:
	    grade = '[0, 3000)'
	elif history_ag.average >= 3000 and history_ag.average < 4000:
	    grade = '[3000, 4000)'
	elif history_ag.average >= 4000 and history_ag.average < 5000:
	    grade = '[4000, 5000)'
	elif history_ag.average >= 5000 and history_ag.average < 6000:
	    grade = '[5000, 6000)'
	else:
	    grade = '[6000,sys.maxint)'
	rates.setdefault(grade, [])
	rates[grade].append(history_ag.increase_rate)

    if ABS:
        for grade in rates:
            print '%s\t%s' % (grade, utils.abs_average(rates[grade]))
    else:
        for grade in rates:
            print '%s\t%s' % (grade, utils.average(rates[grade]))

def print_usage():
    print 'grep -e "Ag" ../history_backup/ag.history | python daily_ranges.py'

if __name__ == '__main__':
    ABS = False
    if len(sys.argv) == 2 and sys.argv[1] == 'abs':
        ABS = True
    reducer(sys.stdin, ABS)

