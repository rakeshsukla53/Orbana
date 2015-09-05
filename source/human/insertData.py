__author__ = 'rakesh'

from itertools import groupby
import collections

phoneNumbers = []

y = open("output.txt", "r")

for line in y:

    phoneNumbers.append(int(line))

counter = collections.Counter(phoneNumbers)

for i in zip(sorted(counter.keys())[::-1], sorted(counter.values())[::-1]):

    print i




