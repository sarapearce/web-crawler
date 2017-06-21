import scrapy
import datetime
import json


class TwitterSpider(scrapy.Spider):
    name = "twitter_crawl"
    mega_list = []

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

        # grab the text of the tweet, for every tweet on the page
        all_tweet_text = response.xpath('//*[contains(@class, "tweet-text")]/text()').extract()

        # loop, grab, and count proper nouns out of the tweets
        for tweet in all_tweet_text:
            # break into words by splitting on whitespace
            words = tweet.split()

            for word in words:
                # use the uppercase first letter as the flag for a proper noun for now
                if word[0].isupper():
                    clean_word = self.cleanWord(word)
                    self.mega_list.append(clean_word)

        # print(self.mega_list)
        list_with_count = self.countWords()

        print(list_with_count)

    def cleanWord(self, word):
        # cleaning process is not optimized, currently looking at every word and every character
        chars_to_remove = [".", "'", "'s", "Retweet", ",", ":", ";", "?", "!", "-"]
        clean_word = []
        for char in chars_to_remove:
            if char in word:
                clean_word = word.replace(char, '')

        cleaned_word = clean_word if clean_word else word

        return cleaned_word

    def countWords(self):
        distinct_words = set(self.mega_list)
        word_count = []
        for word in distinct_words:
            count = self.mega_list.count(word)
            word_count.append((word, count))

        return word_count

    # def buildKey(self, url):
    #     date = datetime.datetime.today().strftime('%Y-%m-%d')
    #     site = url.split("/")[-1]
    #     key = site + '-' + date
    #
    #     return key


        # write output to a file
        # filename = resp
        # with open(filename, 'wb') as f:
        #     f.write(counts_by_site_date)
        # self.log('Saved file %s' % filename)


