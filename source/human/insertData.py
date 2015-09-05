__author__ = 'rakesh'

from itertools import groupby
import collections
import requests


whitePage = 'https://proapi.whitepages.com/2.1/phone.json?api_key=4fe914c0a697d7d1d4db193a1bc50eda&phone_number='

phoneNumbers = []

y = open("output.txt", "r")

for line in y:

    phoneNumbers.append(int(line))

counter = collections.Counter(phoneNumbers)

for i in zip(sorted(counter.keys())[::-1], sorted(counter.values())[::-1]):

    #print i

    phoneNumber, frequency = list(i)[0], list(i)[1]

    areaCode = str(phoneNumber)[0:3]

    print phoneNumber, frequency, areaCode

    Phone.objects.create(phone_number=phoneNumber, area_code=areaCode, frequency=frequency)

    '''
    whitePageLink = whitePage + str(phoneNumber)

    try:

        r = requests.get(str(whitePageLink))

        dict = r.json()

        print dict

        address =  dict['results'][0]['associated_locations'][0]['address']

        latitude =  dict['results'][0]['associated_locations'][0]['lat_long']['latitude']

        longitude = dict['results'][0]['associated_locations'][0]['lat_long']['longitude']

        state_code = dict['results'][0]['associated_locations'][0]['state_code']

        print phoneNumber, areaCode, address, latitude, longitude, state_code

    except:

        pass

    '''





