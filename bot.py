import tweepy
from Poem import Poem
# Uncomment to run tests
# from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

parsed_content = [
    "First tweet of the thread !",
    "Second tweet of the thread !",
    "Third tweet of the thread ! I'm doing great :3"
]

poem = Poem(parsed_content=parsed_content)
poem.tweet(api)