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

        #
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        site = response.url.split("/")[-1]

        # this is unique identifier for each crawl, it is used frequently as a key
        site_date = site + date

        # assign to filename for output
        # filename = '%s-twitter-crawl.html' % site_date


        # loop, grab, and count proper nouns
        proper_nouns = []
        for tweet in all_tweet_text:
            words = tweet.split()

            for word in words:
                # use the uppercase first letter as the flag for a proper noun. not a robust assumption, i know
                if word[0].isupper():
                    proper_nouns.append(word)

        # print('PROPER NOUNS ARRAY')
        # print(proper_nouns)

        # get proper nouns with no repeats
        distinct_proper_nouns = set(proper_nouns)

        noun_count = []
        counts_by_site_date = []
        for noun in distinct_proper_nouns:
            # # clean nouns for counting
            # if "'s" in noun:
            #     noun = noun.replace("'s", "")
            #
            # if "\u2019s" in noun:
            #     noun = noun.replace("\u2019s", "")
            #
            # if "!" in noun:
            #     noun = noun.replace("!", "")

            # this wont work yet because the proper_nouns array does not have clean data
            count = proper_nouns.count(noun)
            noun_count.append((noun, count))

        # counts_by_site_date.append((site_date, noun_count))


        print('COUNTS BY SITE DATE')
        print(counts_by_site_date)

        print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

        # json._default_encoder

        counts_by_site_date_dict = dict(counts_by_site_date)
        jsonObj = json.dumps(counts_by_site_date_dict)
        jsonObj_clean_left = str.replace(jsonObj, "[", "{")
        jsonObj_clean = str.replace(jsonObj_clean_left, "]", "}")
        # print(jsonObj_clean)

        # build the giant json blob for sending to the front end
        # complete_json_blob = {}
        # complete_json_blob[site_date] =
         # write output to a file
         # with open(filename, 'wb') as f:
         #     f.write(counts_by_site_date)
         # self.log('Saved file %s' % filename)
