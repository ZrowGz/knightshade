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
- snscrape

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



---

## Acknowledgements

- Development Team: 
    - [Eamon](https://github.com/zrowgz) 
    - [Lisa](https://github.com/balllisaann)
    - [Meghan](https://github.com/megkennedy)
- snscrape source code was utilized in this app. Follow the links in the Installation section for more details
- MartinBeckUT's Python Wrapped TwitterScraper is the core of how snscrape was integrated into this project.
- Troubleshooting support provided by Kevin Nguyen and [Gerrit Hall](https://github.com/zcor)
