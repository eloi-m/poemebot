import tweepy, time, sys

# Uncomment to run tests
# from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


text_to_red = "helloworld.txt"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(text_to_red, 'r')
f = filename.readlines()
filename.close()

for line in f:
    print("About to tweet !")
    api.update_status(line)
    print("I tweeted :3")
    time.sleep(5)  # Tweet every 60 seconds
