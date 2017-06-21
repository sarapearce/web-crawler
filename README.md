# crawler_v2
Python web crawler for scraping data using Scrapy package.

<em>What This Project Does</em>

This is a Python web crawler. It crawls any website put into the url array in a "spider_name.py" file. It then takes the response from that crawl and parses the data for a json object to go to the front end for display.

<em>Contributing Tech</em>

Architecture: Python 3.5
Scrapy for the web crawler https://scrapy.org/
Some dependencies for Scrapy
Tools used: Scrapy docs, VirtualEnv, IntelliJ, Vagrant

<em>How to Run</em>

Open the twitter_spider.py file in backend/spiders/tutorial/spiders/twitter_spider.py 
In line 10,  add the url(s) for the twitter feed you would like crawled
On command line, cd into the "crawler_v2/crawler/backend folder"
Run "scrapy crawl twitter_crawl". 

The frontend to this project can be found at: https://github.com/sarapearce/crawler-frontend. 
