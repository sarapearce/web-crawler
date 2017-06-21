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

        # current issue: i need the response from this loop to get aggregate counts rather than crawl counts
        # meaning I want to take the returned data and update a dict with it.
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('Begin parsing the response')

        # grab the text of the tweet, for every tweet on the page
        all_tweet_text = response.xpath('//*[contains(@class, "tweet-text")]/text()').extract()

        # loop, grab, and count proper nouns out of the tweets
        proper_nouns = []
        cleaned_words = {}
        for tweet in all_tweet_text:
            # break into words by splitting on whitespace
            words = tweet.split()

            for word in words:
                # use the uppercase first letter as the flag for a proper noun for now
                if word[0].isupper():
                    clean_word = self.cleanWord(word)
                    proper_nouns.append(clean_word)

        key = self.buildKey(response.url)
        cleaned_words[key] = proper_nouns

        return cleaned_words

        # list_with_count = self.getWordCount(proper_nouns)

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

    def buildKey(self, url):
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        site = url.split("/")[-1]
        key = site + '-' + date

        return key


        # write output to a file
        # filename = resp
        # with open(filename, 'wb') as f:
        #     f.write(counts_by_site_date)
        # self.log('Saved file %s' % filename)


