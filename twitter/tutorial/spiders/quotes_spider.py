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
        print('Begin parsing the response')

        # grab html that has a class of tweet-text for parsing
        all_tweet_text = response.xpath('//*[contains(@class, "tweet-text")]/text()').extract()

        # loop, grab, and count proper nouns
        proper_nouns = []
        for tweet in all_tweet_text:
            # break into words by splitting on whitespace, which is the default when nothing is indicated
            words = tweet.split()

            for word in words:
                # use the uppercase first letter as the flag for a proper noun. todo: come up with more conditions for being a proper noun
                if word[0].isupper():
                    proper_nouns.append(word)

        #print('PROPER NOUNS ARRAY')
        #print(proper_nouns)


        noun_count_by_site = []
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        site = response.url.split("/")[-1]
        index = site + '-' + date
        noun_count_by_site.append((index, proper_nouns))

        print(noun_count_by_site)



        # get proper nouns with no repeats
        # distinct_proper_nouns = set(proper_nouns)

        noun_count = []
        counts_by_site_date = []
        # for noun in distinct_proper_nouns:
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
            # count = proper_nouns.count(noun)
            # noun_count.append((noun, count))

        # counts_by_site_date.append((site_date, noun_count))


        #
        # date = datetime.datetime.today().strftime('%Y-%m-%d')
        # site = response.url.split("/")[-1]




        # write output to a file
        # filename = resp
        # with open(filename, 'wb') as f:
        #     f.write(counts_by_site_date)
        # self.log('Saved file %s' % filename)


