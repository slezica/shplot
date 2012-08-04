#!/usr/bin/env python
#-*- coding: utf-8 -*-

import optparse, random, sys, operator
from collections import Counter, namedtuple

HBARS = ('▏', '▎', '▍', '▌', '▋', '▊', '▉', '█')

def hbar(x):
    return HBARS[-1] * (x / len(HBARS)) + HBARS[x % len(HBARS)]

def pad(s, cols):
    return s + (cols - len(s)) * " "

def pair(string):
    key, value = string.split('=', 1)
    return (key, float(value))

def dataset(args):
    return [pair(arg) for arg in args]

def hbars(width, dataset, scale = None):
    max_val  = max(value for key, value in dataset)
    max_klen = max(len(key) for key,value in dataset)
    scale    = width * 8 / (scale or max_val)

    for key, value in dataset:
        value = int(value * scale)
        print pad(key , max_klen), hbar(value)

def start(options, args):
    if len(args) < 1:
        print "Usage: shplot [-w|--width=n] key=value [key2=value2,...]"
    else:
        data = dataset(args)
        hbars(int(options.width), data)

if __name__ == "__main__":
    p = optparse.OptionParser()
    
    p.add_option('--width', '-w', default = '20')

    start(*p.parse_args())

