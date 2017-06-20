import scrapy
import datetime
import json


class TwitterSpider(scrapy.Spider):
    name = "twitter_crawl"

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
                # use the uppercase first letter as the flag for a proper noun. later: come up with more conditions for being a proper noun
                if word[0].isupper():
                    clean_word = self.cleanWord(word)
                    proper_nouns.append(clean_word)

        list_with_count = self.getWordCount(proper_nouns)
        print(list_with_count)

        # date = datetime.datetime.today().strftime('%Y-%m-%d')
        # site = response.url.split("/")[-1]
        # index = site + '-' + date

        # print('PROPER NOUNS ARRAY')
        # print(proper_nouns)

    def cleanWord(self, word):
        # cleaning process is not optimized, currently looking at every word and every character
        chars_to_remove = [".", "'", "'s", "Retweet", ",", ":", ";", "?"]
        clean_word = []
        for char in chars_to_remove:
            if char in word:
                clean_word = word.replace(char, '')

        cleaned_word = clean_word if clean_word else word

        return cleaned_word

    def getWordCount(self, word_list):
        counts_list = []
        distinct_words = set(word_list)

        for word in distinct_words:
            word_count = word_list.count(word)
            counts_list.append([word, word_count])

        return counts_list




        # print out the nouns by site
        # nouns_by_site = []
        # date = datetime.datetime.today().strftime('%Y-%m-%d')
        # site = response.url.split("/")[-1]
        # index = site + '-' + date
        # nouns_by_site.append((index, proper_nouns))
        #
        #
        # print(nouns_by_site)

        # date = datetime.datetime.today().strftime('%Y-%m-%d')
        # site = response.url.split("/")[-1]




        # write output to a file
        # filename = resp
        # with open(filename, 'wb') as f:
        #     f.write(counts_by_site_date)
        # self.log('Saved file %s' % filename)


