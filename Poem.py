import time
class Poem:
    time_between_tweets = 5 # Seconds
    def __init__(self, author = "author", title="title", content ="", parsed_content = []):
        self.author = author
        self.content = content
        self.title = title
        self.parsed_content = parsed_content

    def __repr__(self):
        return f"Poem by {self.author} : {self.title} \n {self.content}"
    def __str__(self):
        return f"Poem by {self.author} : {self.title} \n {self.content}"

    def tweet(self, api):
        if len(self.parsed_content) == 0:
            raise ValueError("Nothing to tweet")
        if len(self.parsed_content) == 1:
            print("About to tweet !")
            api.update_status(self.parsed_content[0])
            print("I tweeted :3")
        else:
            first_status = self.parsed_content[0]
            print("About to tweet the first tweet of the thread !")
            first_tweet = api.update_status(first_status)
            print("I tweeted the first tweet of the thread :3")
            previous_tweet_id = first_tweet.id
            time.sleep(self.time_between_tweets)

            for status in self.parsed_content[1:]:
                print("About to tweet !")
                tweet = api.update_status(status, in_reply_to_status_id = previous_tweet_id)
                print("I tweeted :3")
                previous_tweet_id = tweet.id
                time.sleep(self.time_between_tweets)