__author__ = 'rakesh'

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = 'WQtHRLr2lzfX5YnvrhhPe0ZcI'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'p3kAMerQQDckd0LHMsLyrYEF7YyeWm5IDMge13NzkBdu8xqv4a'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '39455623-O8jZvog8BRfq7qA77IcEZhufnZn6cp9GpFz5pCCEH'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'mCBkPyBFQH2RKSpXlWGmcP2R6iFi1Hr86oAhFuo0zFxCG'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()


for line in f:
    api.update_status(status=line)
    print line
    time.sleep(900)#Tweet every 15 minutes
