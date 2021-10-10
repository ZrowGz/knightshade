# Import libraries
import pandas as pd
from pathlib import Path
import csv
import snscrape.modules.twitter as sntwitter

maxTweets = 25000

csv_file =  open("../data/ltcData.csv", 'w')

csv_writer = csv.writer(csv_file, delimiter=",")

# Scrape the tweets
for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('litecoin since:2021-01-01 until:2021-09-30').get_items()):
    i = i + 1
    if i>maxTweets:
        break
    csv_writer.writerow([tweet.date, tweet.id, tweet.replyCount, tweet.likeCount, tweet.retweetCount, tweet.hashtags, 1])

# This displays ongoing data when ran through the CLI
# Disabled for jupyter notebook use.
#    if i % 10 == 0:
#        print(f"Put {i} tweets into {csv_file}")