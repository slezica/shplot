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
    key, value = tuple(s.strip() for s in string.split('=', 1))
    return (key, float(value))

def dataset(string):
    return dict(pair(subs) for subs in string.split(','))

def datasets(strings):
    return tuple(dataset(s) for s in strings)

def hbars(width, datasets):
    max_val  = max(max(ds.itervalues()) for ds in datasets)
    scale    = width * 8 / max_val

    return _hbars(scale, datasets)

def _hbars(scale, datasets):
    all_keys = reduce(set.union, (set(s.iterkeys()) for s in datasets))
    max_klen = max(map(len, all_keys))

    for key in all_keys:
        first = True
        for dataset in datasets:
            value = int(dataset.get(key, 0) * scale)

            if first: print pad(key, max_klen), hbar(value)
            else:     print pad("" , max_klen), hbar(value)

            first = False

def start(options, args):
    data = datasets(args)
    hbars(int(options.width), data)

if __name__ == "__main__":
    p = optparse.OptionParser()
    
    p.add_option('--width', '-w', default = '10')

    start(*p.parse_args())

