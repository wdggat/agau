#!/usr/bin/env python 
#!-*- coding: utf-8-*-

import utils

# 品种 银行买入价	 银行卖出价	 中间价	 最高中间价	 最低中间价
class Paper():
    def __init__(self, kind, bank_buy, bank_sell, price, high, low, time):
        self.kind = kind
        self.bank_buy = float(bank_buy)
	self.bank_sell = float(bank_sell)
	self.price = float(price)
	self.high = float(high)
	self.low = float(low)
	self.time = time
	self.dt = utils.get_datetime(time)
	self.day = utils.get_paper_day(self.dt)

    @classmethod
    def get_from_paperline(self, line):
        items = line.strip().split('\t')
	return Paper(items[0], items[1], items[2], items[3], items[4], items[5], items[6])
