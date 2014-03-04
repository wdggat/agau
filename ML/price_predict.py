#!/usr/bin/env python
#-*-coding: utf8 -*-

import sys 

def reducer(lines, value_len):
    domain = [(-100, 100)] * value_len + [(-2000, 2000)]
    for line in lines:
        items = line.strip().split()
	if len(items) != value_len: continue
	# TODO

def print_usage():
    print 'Usage:'
    print '\tpython price_predict.py <LENGTH>'

if __name__ == '__main__':
    
