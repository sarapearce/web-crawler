import logging
import scrapy
import datetime
import json


class QuotesSpider(scrapy.Spider):
    name = "media_aggregate"

    def start_requests(self):
        urls = [
            'https://twitter.com/nytimes', 'https://twitter.com/AP', 'https://twitter.com/AJEnglish',
            'https://twitter.com/CNN', 'https://twitter.com/ABC', 'https://twitter.com/CBSNews',
            'https://twitter.com/FoxNews', 'https://twitter.com/FoxBusiness', 'https://twitter.com/NBCNewsBusiness'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        logging.info('Begin parsing the response')
        # grab html that has a class of tweet-text for parsing
        all_tweet_text = response.xpath('//*[contains(@class, "tweet-text")]/text()').extract()
        logging.info('ALL TWEET TEXT')
        print(all_tweet_text)

        date = datetime.datetime.today().strftime('%Y-%m-%d')
        site = response.url.split("/")[-1]
        site_date = site + date
        filename = '%s-twitter-crawl.html' % site_date
        cleaned_array = []
        all_cleaned_by_website = dict()
        for tweet in all_tweet_text:
            logging.info('INSIDE THE CLEANING LOOP')
            if tweet[0].isalpha():
                cleaned_array.append(tweet)

        all_cleaned_by_website.update({site_date : cleaned_array})
        # possibly generate dict keyed on website name. push into large json

        with open(filename, 'wb') as f:
            f.write(all_cleaned_by_website)
        self.log('Saved file %s' % filename)
