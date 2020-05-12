import tweepy
import schedule
import time
import random
from datetime import datetime

from Poem import Poem
from Poem_database import Poem_database, db

# Uncomment to run tests
# from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


# Connect to API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Connect to database
all_non_tweeted_poems = Poem_database.query.filter_by(tweeted=False).all()
random_poem = random.choice(all_non_tweeted_poems)


poem = Poem(
    author=random_poem.author,
    title=random_poem.title,
    content=random_poem.content
)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"Current Time : {current_time}")


print(f"Poem {poem.title} \n {poem.content}")
poem.parse()
print(f"Parsed poem {poem.title}: \n ")
print(*poem.parsed_content, sep="\n + ")


def job():
    try:
        poem.tweet(api)
        random_poem.tweeted = True
        db.session.commit()
    except:
        raise ValueError("Something append")


schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
