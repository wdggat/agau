#!/usr/bin/python 

import sys

def main(lines):
    # month,open,close,highest,lowest
    years, monthes, changes = set(), set(), {}
    for line in lines:
        [first_day,openprice,close,highest,lowest] = line.strip().split()
	[year, month] = first_day.split('-')[0:2]
	years.add(year)
	monthes.add(month)
	change = '-'
	if float(close) >= float(openprice):
	    change = '+'
	changes.setdefault(year, {})
	changes.get(year, {})[month] = change

    print '\t%s' % ('\t'.join(sorted(years)))
    for month in sorted(monthes):
        print month + '\t',
        for year in sorted(years):
	    print changes.get(year).get(month, '') + "\t",
	print '\n',

if __name__ == '__main__':
    main(sys.stdin)

