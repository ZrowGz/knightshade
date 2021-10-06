# knightshade

### tweetsAnalysis.ipynb 
Running the data retrieval and clean up in here.
Needing help figuring out how to get rid of specific portions of the date time. I could proabably normalize it to midnight and just get rid of all the time parts, but that's a lot of data loss! It'd be sweet to group by like hourly. Think it matters?


### btcHashTweets.py 
This is one I can run from VS code and it generates a nice json file. But we probably don't actually need all that data so might as well trash it yeah?

### /data 
This is where I was going to store a sql database, but I ended up just going from scraper to list, to dataframe. If we want to store the data, we should probably take it into sql for more efficient storage since only 5000 tweets took a megabyte. 5M tweets will be a gb by csv unless we shed all that extra data.

Speaking of that, **do we actually want all of the datapoints I'd pulled out from twitter?** If not, which should I keep?