
"""
import snscrape.modules.twitter as twitterScraper

scraper = twitterScraper.TwitterHashtagScraper("bitcoin")

max_tweets = 5

for i,tweet in enumerate(scraper.get_items()):
    if i > max_tweets:
        break
print(f"Found {i} tweets. The most recent one is from {tweet.date} and says: {tweet.content}")



import os

# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --max-results 10 twitter-hashtag 'bitcoin'> tweets.json")

"""
import os
# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --progress --max-results 500 --since 2020-05-01 twitter-hashtag \"bitcoin until:2020-07-31\" > tweets.json")