# crawler_v2
Python web crawler for scraping data using Scrapy package.

What This Project Does 

This is a Python web crawler. It crawls any website put into the url array in the quotes_spider.py file. It then takes the response from that crawl and parses the data for a json object to go to the front end for display. 

Contributing Tech  

Architecture:  Python 3.5
Scrapy for the web crawler https://scrapy.org/
Some dependencies for Scrapy
Tools used: Scrapy docs, VirtualEnv, IntelliJ, Vagrant

How to Run

Open the quotes_spider.py file in twitter/tutorial/spiders/quotes_spider.py
In line 10,  add the url for the twitter feed you would like crawled
On command line, cd into the "crawler_v2/crawler/twitter folder"
Run "scrapy crawl media_aggregate"

Currently output is printing into the terminal window. The next phase is getting the JSON shipped to the front end with a simple button push and data return for the front end. That will be made with Django.
