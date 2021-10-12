### App to interface with snscrape using command line user selections

# Import libraries and modules
import snscrape.modules.twitter as sntwitter
# install the following modules?
import questionary
import time
#  pip install python-dateutil
from dateutil import parser

# Initialize the needed variables
selectedData = []
tweets_list = []
totalTime = 0
i = 0
start = 0

# Available Tweet data to select from
url = 'url'
date = 'date'
content = 'renderedContent'
tweetId = 'id'
user = 'user'
replies = 'replyCount'
retweets = 'retweetCount'
likes = 'likeCount'
quotes = 'quoteCount'
conversation = 'conversationId'
language = 'lang'
source = 'source'
sourceUrl = 'sourceUrl'
sourceLabel = 'sourceLabel'
outlinks = 'outlinks'
tcooutlinks = 'tcooutlinks'
media = 'media'
retweetedTweet = 'retweetedTweet'
quoted = 'quotedTweet'
replyToTweet = 'inReplyToTweetId'
replyToUser = 'inReplyToUser'
usersMentioned = 'mentionedUsers'
latlong = 'coordinates'
place = 'place'
hashtags = 'hashtags'
cashtags = 'cashtags'

##### MIGHT NEED TO MOVE ALL THE QUESTIONS INTO THE RUN FUNCTION, OR SET A COUNTER AND IF IT'S BEEN RAN ONCE, JUST GO TO WRITING DATA
def run(tweets_list, selectedData, begin_date, finish_date, statFrequency, searchTerm, outputMethod, totalTime, i, start):
    # Start the clock
    start = int(time.time())
    csv_writer.writerow(selectedData)
    # Scrape the Twitter
    for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'{searchTerm} since:{finish_date} until:{begin_date}').get_items()):
        # Increase counter and display tweet stats
        i = i + 1
        # Create an empty list for storing the parameters
        searchParams = []
        # Check that tweet limit hasn't been reached. If reached, terminate search.
        if i > tweetMax:
            break
        for value in selectedData: 
            searchParams.append(getattr(tweet, value))
        searchParams.append(1)
        # Output the tweet data in the required format
        if outputMethod == True:
            csv_writer.writerow(searchParams)
        else:
            tweets_list.append(searchParams)
        
        # Check if it is time to display stats, and if so, calculate the data and display it.
        if i % statFrequency == 0:
            now = int(time.time())
            totalTime = now - start
            avgRate = i / totalTime       
            print(f'Found {i} tweets in {totalTime:.0f} seconds, {avgRate:.0f} tweets per second')

    return(totalTime, i, tweets_list)

# Enter the output file path
filePath= questionary.path('Enter the desired path & name of the output file.').ask()

# Select the data output method
outputMethod = questionary.confirm('Save as .csv: Yes. Otherwise, store in pandas DataFrame.').ask()
if outputMethod == True:
    # Import csv libraries
    import csv
    from pathlib import Path
    # Set up the .csv output method
    # Create CSV file and path to write to
    csv_file =  open(filePath, 'w')
    # Activate csv.writer
    csv_writer = csv.writer(csv_file, delimiter=",")
else:
    import pandas as pd

# Get the search term
searchTerm = questionary.text('Type the word/phrase/name you wish to search for (hashtags should not include "#"').ask()

# Select Tweet data to scrape
# Select all data or select specific data?
selectAllData = questionary.confirm(
    'Yes, Select all tweet data? (WARN: May create large files!) or No, let me pick specific data.'
).ask()

if selectAllData == True:
    selectedData = [
        url, date, content, tweetId, user, replies, retweets, likes, quotes, conversation,
        language, source, sourceUrl, sourceLabel, outlinks, tcooutlinks, media, retweetedTweet,
        quoted, replyToTweet, replyToUser, usersMentioned, latlong, place, hashtags, cashtags
    ]
else:
    selectedData = questionary.checkbox(
    'Select the data you want to collect:',
    choices=[
        url, date, content, tweetId, user, replies, retweets, likes, quotes, conversation,
        language, source, sourceUrl, sourceLabel, outlinks, tcooutlinks, media, retweetedTweet,
        quoted, replyToTweet, replyToUser, usersMentioned, latlong, place, hashtags, cashtags
    ]).ask()
    #tweets_list = []
    

# User to input frequency to see cli update messages, per tweet count
statFrequency = int(questionary.select(
    'How frequently do you want to be updated on tweet counts?',
    choices=['10', '100', '250', '500', '1000', '2500', '5000', '10000']
).ask())

# Select dates
begin_date = questionary.text('''Dates start from closest to now and run backwards. 
    Enter date to begin search at as: YYYY-MM-DD or YYYY-MM-DDThh:mm:ss+00:00 (where "+00:00" is UTC)''').ask()
begin_date = parser.parse(begin_date)

finish_date = questionary.text('''Dates start from closest to now and run backwards. 
    Enter date to complete search at as: YYYY-MM-DD or YYYY-MM-DDThh:mm:ss+00:00 (where "+00:00" is UTC)''').ask()
finish_date = parser.parse(finish_date)

# Enter the maximum number of tweets to find
includeTweetMax = questionary.confirm('Include a tweet limit?').ask()
if includeTweetMax == True:
    tweetMax = int(questionary.text('How many tweets to cap the search at?').ask())
else:
    tweetMax = 99999999999999999999


# Scrape the tweets
run(tweets_list, selectedData, begin_date, finish_date, statFrequency, searchTerm, outputMethod, totalTime, i, start)


# At the end of the scrape event, display final stats
if outputMethod == True:
    print(f'Scraping complete. Total tweet count: {i}, elapsed time: {totalTime:.0f}.')
else:
    print(f'Scraping complete. Total tweet count: {i}, elapsed time: {totalTime:.0f}.')
    tweets_df = pd.DataFrame(tweets_list, columns=selectedData)
    tweets_df
