import tweepy, time, sys

# Uncomment to run tests
# from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


text_to_read = "helloworld.txt"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(text_to_read, 'r')
f = filename.readlines()
filename.close()

first_status = f[0]
print("About to start the thread !")
first_tweet = api.update_status(first_status)
print("I tweeted the first tweet of the thread :3")

previous_tweet_id = first_tweet.id
time.sleep(5)

if len(f) > 0:
    for status in f[1:]:
        print("About to tweet !")
        tweet = api.update_status(status, in_reply_to_status_id = previous_tweet_id)
        print("I tweeted :3")
        previous_tweet_id = tweet.id

        time.sleep(5) # wait 5 secs