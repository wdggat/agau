#!/usr/bin/env python 
#!-*- coding: utf-8-*-

import utils

# 品种	 当前价	  涨跌幅	 成交量(手)	 开盘价	 昨收价	 最高价	 最低价	 更新时间
class Agau():
    def __init__(self, kind, price, increase, dealed, open_price, closed_price, high, low, time):
        self.kind = kind
	self.price = float(price)
	self.increase = float(increase.strip('%')) / 100
	self.dealed = int(dealed)
	self.open_price = float(open_price)
	self.closed_price = float(closed_price)
	self.high = float(high)
	self.low = float(low)
	self.time = time
	self.dt = utils.get_datetime(time)
	self.day = utils.get_agau_day(self.dt)

    @classmethod
    def get_from_agauline(self, line):
        items = line.strip().split('\t')
	return Agau(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8])
