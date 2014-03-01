#!/usr/bin/env python 
#-*-coding: utf-8 -*-

import sys 

#交易品种 日期 开盘价 最新价 昨结算 最高价 最低价 收盘价 涨跌（元） 涨跌幅 加权平均价 成交量（千克） 成交金额（元） 持仓量 交收方向
class History():
    def __init__(self, kind, day, open_price, price_now, closed_price, high, low, closed_today, increase, increase_rate, average, dealed_num, dealed_money, hold, pay_direction):
        self.kind = kind
	self.day = day
	self.open_price = float(open_price.replace(',',''))
	self.price_now = float(price_now.replace(',',''))
	self.closed_price = float(closed_price.replace(',',''))
	self.high = float(high.replace(',',''))
	self.low = float(low.replace(',',''))
	self.closed_today = float(closed_today.replace(',',''))
	self.increase = float(increase.replace(',',''))
	self.increase_rate = float(increase_rate.strip('%')) / 100
	self.average = float(average.replace(',',''))
	self.dealed_num = float(dealed_num.replace(',',''))
	self.dealed_money = float(dealed_money.replace(',',''))
	self.hold = float(hold.replace(',',''))
	self.pay_direction = pay_direction

    @classmethod
    def get_from_historyline(self, line):
        items = line.strip().split()
	return History(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8], items[9], items[10], items[11], items[12], items[13], items[14])
	
