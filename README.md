
## What This Project Does ##

This is a Python web crawler that I use to scrape data from any webpage where scraping is allowed. It crawls any website put into the url array in a `my_spider_name.py` file. It then takes the response from that crawl and parses the data for a json object to go to the front end for display.

## Contributing Tech ##

Architecture: Python 3.5
Scrapy for the web crawler https://scrapy.org/ <br>
<br>

## How to Run ##

`cd /spiders/tutorial/spiders` <br> 
`vi twitter_spider.py` <br>
Around line 10,  add the url(s) for the twitter feed(s) you would like crawled <br>
go back up a directory `cd ..` <br>
Run `scrapy crawl twitter_crawl`. <br>

## Support Materials and Initial Codebases ##
https://doc.scrapy.org/en/latest/intro/tutorial.html

