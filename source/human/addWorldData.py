__author__ = 'rakesh'

import collections

#from human.models import Phone, State

y = open("../worldData", 'r')

for line in y:

    value = line.split('@')
    phoneNumber = value[0]


