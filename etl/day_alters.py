#!/usr/bin/env python

import sys
from history import History
sys.path.append('../ML/')
import pydrawer
import math

def reducer(lines):
    positives, negatives, alters = [], [], []
    for line in lines:
        history_record = History.get_from_historyline(line)
        if history_record.increase > 0:
	    positives.append(history_record.increase)
	    if len(negatives) != 0:
		alters.append(sum(negatives))
		negatives = []
	elif history_record.increase < 0:
	    negatives.append(history_record.increase)
	    if len(positives) != 0:
		alters.append(sum(positives))
		positives = []

    if len(positives) != 0:
        alters.append(sum(positives))
    elif len(negatives) != 0:
        alters.append(sum(negatives))

    odd_200 = float(sum([1 for alter in alters if abs(alter) <= 200])) / len(alters)

    print 'alters: %s, odd_200: %f' % (alters, odd_200)
    pydrawer.draw(alters, 'bo')

if __name__ == '__main__':
    reducer(sys.stdin)

