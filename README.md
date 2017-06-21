# crawler_v2
Python web crawler for scraping data using Scrapy package.

<h3>What This Project Does</h3>

This is a Python web crawler. It crawls any website put into the url array in a "spider_name.py" file. It then takes the response from that crawl and parses the data for a json object to go to the front end for display.

<h3>Contributing Tech</h3>

Architecture: Python 3.5
Scrapy for the web crawler https://scrapy.org/ <br>
Some dependencies (~5) for Scrapy <br>
Tools used: Python, Scrapy, VirtualEnv, IntelliJ, Vagrant <br>

<h3>How to Run</h3>

Open the twitter_spider.py file in backend/spiders/tutorial/spiders/twitter_spider.py 
Around line 10,  add the url(s) for the twitter feed you would like crawled
On command line, cd into the crawler_v2/backend/spiders folder
Run "scrapy crawl twitter_crawl". 

The frontend to this project can be found at: https://github.com/sarapearce/crawler-frontend. 
