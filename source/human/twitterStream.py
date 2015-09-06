__author__ = 'rakesh'

import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'ye3ZhuewkvXukV3wVR2psAeDd'
consumer_secret = 'w2jSLL5DfILpljqokWLC0yehhLFFVMk6MtY0df6SV9atovFROD'
access_token = '39455623-XuCaEN3XcalYkHXW7XHbEpoXRDETRhON4uofKffp7'
access_token_secret = 'AQPvUVN8uFPSZnszQmYDvGGCXBscu4HbsDO06GYhAV3cN'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users

        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''


    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=["Trafficking"])

