#!/usr/bin/env python

import matplotlib.pyplot as plt

def draw(*args, **kargs):
    plt.grid(True)
    plt.ylabel('hello, boy')
    plt.plot(*args, **kargs)
    plt.show()

def draw_dates(dates, b):
    plt.plot_date(dates, b)
    plt.show()

if __name__ == '__main__':
    a = [1,2,3,4,5]
    b = [10,20,30,40,50]
    c = [15,25,35,45,55]
    d = [18,28,38,48,58]
    #draw(a, b)
    ndraw(a, b, 'r-', a, c, 'bo', a, d, 'g-')
    #plt.grid(True)
    #plt.plot(a, b, 'r-', a, c, 'bo', a, d, 'g-')
    #plt.show()
