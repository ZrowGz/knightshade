# Import libraries
import pandas as pd
from pathlib import Path
import csv
import snscrape.modules.twitter as sntwitter

csv_file =  open("../large_data/ltcHashData2020.csv", 'w')

csv_writer = csv.writer(csv_file, delimiter=",")

# Scrape the tweets
for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('litecoin since:2020-05-01 until:2021-01-01').get_items()):
    i = i + 1
    csv_writer.writerow([tweet.date, tweet.id, tweet.replyCount, tweet.likeCount, tweet.retweetCount, tweet.hashtags, 1])
    
    if i % 250 == 0:
        print(f"Found {i} tweets so far...")
print(f"Total tweets found for the month: {i}")