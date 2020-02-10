import tweepy, time, sys

from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

argfile = str(sys.argv[1])

# enter the corresponding information from your Twitter application:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    print("About to tweet !")
    api.update_status(line)
    print("I tweeted :3")
    time.sleep(60)  # Tweet every 60 seconds
