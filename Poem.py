import time
import re

CHARACTERS_IN_A_TWEET = 280


def uses_double_newlines_every_time(text):
    newlines = re.findall("\n+", text)
    min_newlines = 2
    for i in range(len(newlines)):
        count_newlines = len(re.findall("\n", newlines[i]))
        if count_newlines < min_newlines:
            return False
    return True


def can_split_in_two(lines):
    n = len(lines)
    assert (n % 2 == 0)
    if count_characters(lines[n // 2:]) < CHARACTERS_IN_A_TWEET and count_characters(
            lines[:n // 2]) < CHARACTERS_IN_A_TWEET:
        return True
    return False


def split_in_two(lines):
    n = len(lines)
    assert (n % 2 == 0)
    new_chunk_1 = "".join(line + "\n" for line in lines[:n // 2])
    new_chunk_2 = "".join(line + "\n" for line in lines[n // 2:])
    return new_chunk_1, new_chunk_2


def count_characters(object):
    if isinstance(object, list):
        sum = 0
        for line in object:
            sum = sum + len(line)
        return sum
    else:
        return len(object)


def can_split_in_chunks_of_size(m, lines):
    # Dividing the list "lines" in chunks of size m
    chunks = [lines[i:i + m] for i in range(0, len(lines), m)]
    for chunk in chunks:
        if count_characters(chunk) > CHARACTERS_IN_A_TWEET:
            return False
    return True


def split_in_chunks_of_size(m, lines):
    chunks_list = [lines[i:i + m] for i in range(0, len(lines), m)]
    chunks = []
    for chunk in chunks_list:
        chunks.append(f"".join(f"{line}\n" for line in chunk))
    return chunks


class Poem:
    time_between_tweets = 5  # Seconds

    def __init__(self, author="author", title="title", content="", parsed_content=[]):
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
            print(f"About to tweet this ! \n {self.parsed_content[0]}")
            api.update_status(self.parsed_content[0])
            print("I tweeted :3")
        else:
            first_status = self.parsed_content[0]
            print(f"About to tweet the first tweet of the thread ! \n {self.parsed_content[0]}")
            first_tweet = api.update_status(first_status)
            print("I tweeted the first tweet of the thread :3")
            previous_tweet_id = first_tweet.id
            time.sleep(self.time_between_tweets)

            for status in self.parsed_content[1:]:
                print(f"About to tweet this ! \n {status}")
                tweet = api.update_status(status, in_reply_to_status_id=previous_tweet_id)
                print("I tweeted :3")
                previous_tweet_id = tweet.id
                time.sleep(self.time_between_tweets)
            print("Everything is tweeted !")
    def parse(self):
        self.parsed_content = []
        divided_in_two = False
        divided_in_even_chunks = False

        last_tweet = f"{self.title}, {self.author}"
        # It's unlikely this tweet is too long, but just in case...
        if len(last_tweet) > CHARACTERS_IN_A_TWEET:
            print("Last tweet is too long")
            last_tweet = last_tweet[0:CHARACTERS_IN_A_TWEET]

        raw_text = self.content.replace("\n\r\n", "\n\n")

        # Check if the poem uses double newlines every single time.
        print(f"Does the poem uses double newlines : {uses_double_newlines_every_time(raw_text)}")
        if uses_double_newlines_every_time(raw_text):
            # If it does, replace every "\n\n" by "\n".
            raw_text = raw_text.replace("\n\n", "\n").replace("\n\n\n", "\n\n")

        # Split along the paragraphs
        paragraphs = raw_text.split("\n\n")

        # Ban useless first lines
        banned_first_lines = ["Sonnet."]
        if paragraphs[0] in banned_first_lines:
            del paragraphs[0]

        # If the first paragraph is a single line, it's likely a title. In that case, join the first 2 paragraphs :
        if len(paragraphs) > 1 and len(paragraphs[0].splitlines()) == 1:
            print("First paragraph looks like a title")
            title = paragraphs[0].splitlines()[0]
            first_paragraph = paragraphs[1]
            title_first_paragraph = "".join((title, "\n", first_paragraph))
            if len(title_first_paragraph) > CHARACTERS_IN_A_TWEET:
                print("I can't join the title and the first part of the poem")
            else:
                del paragraphs[0]
                paragraphs[0] = title_first_paragraph
                print("I joined the title and the first part of the poem")

        # Check length of tweets
        for paragraph in paragraphs:
            # If the paragraph can't be tweeted, I need to split it in a way that makes sens
            if len(paragraph) > CHARACTERS_IN_A_TWEET:
                print(f"This chunk : {paragraph} \n is too big, here's what I'm doing about it")
                lines = paragraph.splitlines()
                n = len(lines)
                # If number of lines is even and I can split the chunk in 2, that's what I do :
                if n % 2 == 0 and can_split_in_two(lines):
                    print(f"I split it in two")
                    divided_in_two = True
                    for tweetable_chunk in split_in_two(lines):
                        self.parsed_content.append(tweetable_chunk)
                if not divided_in_two:
                    for m in [8, 4, 2]:
                        if can_split_in_chunks_of_size(m, lines):
                            divided_in_even_chunks = True
                            print(f"I split it in chunks of size {m}")
                            chunks = split_in_chunks_of_size(m, lines)
                            print(f"tweetable chunk:{chunks}")
                            for chunk in chunks:
                                self.parsed_content.append(chunk)
                            break
                if not divided_in_two and not divided_in_even_chunks:
                    # If the previous divisions don't work, I try to tweet individual lines.
                    for line in lines:
                        if count_characters(line) < CHARACTERS_IN_A_TWEET:
                            print("I'm tweeting it line by line")
                            self.parsed_content.append(line)
                        else:
                            # If the line can't be tweeted, I first try to split it into sentences, and tweet those :
                            sentences = line.split(".")
                            # To remove empty strings
                            sentences = [x for x in sentences if x not in ["", " "]]
                            tweet = f""
                            for index_sentence, sentence in enumerate(sentences):
                                if count_characters(sentence) < CHARACTERS_IN_A_TWEET:
                                    if count_characters(tweet) + count_characters(sentence) <= CHARACTERS_IN_A_TWEET:
                                        if not tweet:
                                            tweet = f"{sentence}"
                                        elif tweet:
                                            tweet = f"{tweet}.{sentence}"
                                        if index_sentence == len(sentences) - 1:
                                            self.parsed_content.append(f"{tweet}.")
                                            tweet = f""
                                    else:
                                        self.parsed_content.append(f"{tweet}.")
                                        tweet = f"{sentence}"
                                else:
                                    # If the sentence is too long, I split into individual words.
                                    words = sentence.split()
                                    tweet = f""
                                    for index_word, word in enumerate(words):
                                        if count_characters(word) < CHARACTERS_IN_A_TWEET:
                                            if count_characters(tweet) + count_characters(
                                                    word) <= CHARACTERS_IN_A_TWEET:
                                                if not tweet:
                                                    tweet = f"{word}"
                                                elif tweet:
                                                    tweet = f"{tweet} {word}"
                                                if index_word == len(words) - 1:
                                                    self.parsed_content.append(f"{tweet}.")
                                                    tweet = f""
                                            else:
                                                self.parsed_content.append(f"{tweet}")
                                                tweet = f"{word}"
                                        else:
                                            # If the word is too long, I split it into letters
                                            letters = list(word)
                                            tweets = [letters[i:i + CHARACTERS_IN_A_TWEET] for i in
                                                      range(0, len(letters), CHARACTERS_IN_A_TWEET)]
                                            tweets = ["".join(tweet) for tweet in tweets]
                                            for tweet in tweets:
                                                self.parsed_content.append(tweet)
            # If the paragraph can be tweeted, it's all good!
            else:
                self.parsed_content.append(paragraph)

        self.parsed_content.append(last_tweet)
