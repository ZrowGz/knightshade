# knightshade

### tweetsAnalysis.ipynb 
Running the data retrieval and clean up in here.
Needing help figuring out how to get rid of specific portions of the date time. I could proabably normalize it to midnight and just get rid of all the time parts, but that's a lot of data loss! It'd be sweet to group by like hourly. Think it matters?


### btcHashTweets.py 
This is one I can run from VS code and it generates a nice json file. But we probably don't actually need all that data so might as well trash it yeah?

### /data 
This is where I was going to store a sql database, but I ended up just going from scraper to list, to dataframe. If we want to store the data, we should probably take it into sql for more efficient storage since only 5000 tweets took a megabyte. 5M tweets will be a gb by csv unless we shed all that extra data.

Speaking of that, **do we actually want all of the datapoints I'd pulled out from twitter?** If not, which should I keep?

---

## Requirements

App Requirements
- Python 3.8
- Jupyter Notebooks/Jupyter Labs
- Recommended to use a conda environment
- snscrape (developer installation)

Python Modules
- pandas
- dotenv
- os
- pathlib
- hvplot
- datetime
- csv
- numpy
- quandl
- fire
- questionary

---

## Installation

### Install snscrape
Follow the directions on installing the developer version of snscrape.  
- Original GitHub repo: 
- Wrapped version (recommended): [TwitterScraper](https://github.com/MartinBeckUT/TwitterScraper.git)

---

## Use

The process of scraping Twitter for commonly used terms can yield extremely large results.  
In order to obtain an adequate time scale to perform analysis upon, millions of tweets were retrieved. Performing these scraping actions from within the Jupyter Notebook for any large sample size will likely take many hours and lead to system instability & data loss. The apps set up in the notebook are for demonstrations only and are not the recommended method of utilizing snscrape.  

### Recommended dataset retrieval

The CLI version of the Twitter Scraper allows for running multiple instances. A version is included in this repo for use on this project specifically, but the main [repo](https://github.com/ZrowGz/EnhancedTwitterScraper.git) may contain future updates.

### Running The Full App
Open the file `RunApps.ipynb`  

As you run each step, it may take some time as some of the data being collected and processed can be substantial in size. As it goes through the process, you will be given updates showing what has been done.

The tweet scraper and csv reader modules are set up to utilize files that are not included with this repository, due to the file size limitations (the bitcoin data was 1.54GB), and in running the tweet reader module, you will only generate a small number of tweet data.  
  
- To generate larger numbers of tweets, you can refer to the `TweetScraperQuest.py` section, or you can modify the `tweetMax = <insert desired tweet count here>`  
- Adjust the file paths for the tweet data you scrape based upon where you save it. It is recommended to adjust all files to the `data` directory, both within the tweet scraping app(s) and the csv processing app. 
- Ensure that you also adjust the file names such that it will be able to locate the file!

Running the data visualizations will use our condensed data as a demonstration. If adding your own data, work through the file and adjust dates and names accordingly.

---

## DISCLAIMERS

Additionally, the `analysis.md` file is a static file and is strictly our interpretation of the results from this project. None of this is financial advice. Do not use our data to place trades. Do not get rugged. Do your own research. Get a hardware wallet and backup your seedphrase in a secure, non-digital manner. **NEVER SHARE YOUR SEED PHRASE WITH ANYONE, EVER, END OF STORY**

---

## Acknowledgements

- Development Team: 
    - [Eamon](https://github.com/zrowgz) 
    - [Lisa](https://github.com/balllisaann)
    - [Meghan](https://github.com/megkennedy)
- snscrape source code was utilized in this app. Follow the links in the Installation section for more details
- MartinBeckUT's Python Wrapped TwitterScraper is the core of how snscrape was integrated into this project.
- Troubleshooting support provided by Kevin Nguyen and [Gerrit Hall](https://github.com/zcor)
