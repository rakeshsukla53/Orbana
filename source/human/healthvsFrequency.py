__author__ = 'rakesh'

import re

y = open('../healthData.txt', 'r')

ranking = []

for line in y:

    state = re.search(r'\w+', line)
    rank = re.search(r'\d+', line)
    if state and rank:
        ranking.append((state.group(), rank.group()))

from operator import itemgetter

ranking.sort(key=itemgetter(1), reverse=True)

ranking.sort(key=itemgetter(0))

newRank = []

for key in ranking:

    newRank.append(key[1])

print newRank


'''
try:
    data = line.split()
    state.append((data[0], data[1]))
except IndexError:
    pass

from operator import itemgetter

state.sort(key=itemgetter(1), reverse=True)

state.sort(key=itemgetter(0))

newState = []

for k in list(set(state)):

newState.append(k[0])


print list(set(newState))

K = [1, 2, 3]

L = ['D', 'B', 'D']

finalList = []

for line in zip(L, K):

finalList.append(line)

print finalList

from operator import itemgetter

finalList.sort(key=itemgetter(1), reverse=True)

finalList.sort(key=itemgetter(0))

print finalList
'''


