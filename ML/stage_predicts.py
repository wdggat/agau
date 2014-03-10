#!/usr/bin/env python

import sys
sys.path.append('../etl/')
import utils
import price_predict
import adjuster

#--NIGHT^	NIGHT$-^	--AM^	AM^-$	--PM^	PM^-$
def reducer(lines, stage_predicts_tempf):
    titles = '--NIGHT^        NIGHT$-^        --AM^   AM^-$   --PM^   PM^-$'.split()
    same = {}
    subsets = utils.subsets(range(len(titles)))
    for subset in subsets:
        # abs(--PM^) is too small
        if len(subset) < 2 or subset[-1] == 4: continue
	command = 'cat %s | cut -f%s > stage_temp.cut' % (stage_predicts_tempf, ','.join([str(i + 1) for i in subset]))
	utils.execute(command)
	solution = price_predict.reducer(open('stage_temp.cut'), adjuster.get_adjuster('STAGE_%d' % len(subset)))
	print 'Title: %s, Solution: %s' % ([titles[i] for i in subset], solution)

def print_usage():
    print 'grep -e "NO" ../etl/stage_alters.ag -v | cut -f3,4,5,6,7,8 > stage_predicts.temp; python stage_predicts.py stage_predicts.temp'

if __name__ == '__main__':
    reducer(sys.stdin, sys.argv[1])

