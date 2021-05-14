#!/usr/bin/env python
import sys
import string

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # make lower casee
    line = line.lower()

    # remove punctuation
    line = line.translate(None, string.punctuation)

    # split the line into words; splits on any whitespace
    words = line.split()

    stops = set(['the','and'])

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stops:
         print '%s\t%s' % (word, "1")
