# crawler_v2
Python web crawler for scraping data using Scrapy package.

<h3>What This Project Does</h3>

This is a Python web crawler. It crawls any website put into the url array in a <code>my_spider_name.py</code> file. It then takes the response from that crawl and parses the data for a json object to go to the front end for display.

<h3>Contributing Tech</h3>

Architecture: Python 3.5
Scrapy for the web crawler https://scrapy.org/ <br>
Some dependencies (~5) for Scrapy <br>
Tools used: Python, Scrapy, VirtualEnv, IntelliJ, Vagrant <br>

<h3>How to Run</h3>

<code>cd backend/spiders/tutorial/spiders</code> <br>
<code>vi twitter_spider.py</code> <br>
Around line 10,  add the url(s) for the twitter feed(s) you would like crawled <br>
go back up a directory <code>cd ../</code> <br>
Run <code>scrapy crawl twitter_crawl</code>. <br>

The frontend to this project can be found at: https://github.com/sarapearce/crawler-frontend. 
