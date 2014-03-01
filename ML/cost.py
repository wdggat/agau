#!/usr/bin/env python

# params: actuals = {'actual' : expected}
def cost(actuals):
    return sum([pow(actual - actuals[actual], 2)])
        
