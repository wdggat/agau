#!/usr/bin/env python 

import sys
import utils
from agau import Agau 

def reducer(lines):
    for line in lines:
        agtd = Agau.get_from_agauline(line)
        

if __name__ == '__main__':
    reducer(sys.stdin)

