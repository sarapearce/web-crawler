import scrapy
import json


class TwitterSpider(scrapy.Spider):
    name = "twitter_crawl"
    mega_list = []
    urls_count = ''
    i = 0

    def start_requests(self):
        urls = [
            'https://twitter.com/nytimes', 'https://twitter.com/AP', 'https://twitter.com/AJEnglish',
            'https://twitter.com/CNN', 'https://twitter.com/ABC', 'https://twitter.com/CBSNews',
            'https://twitter.com/FoxNews', 'https://twitter.com/FoxBusiness', 'https://twitter.com/NBCNewsBusiness'
        ]

        self.urls_count = len(urls)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # currently using a counter in here as a fix for not being able to access the generators in start_requests
        # and unable to replace the yield without breaking Scrapy.
        self.i += 1
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

        # if we are on the last url, then build the json
        if self.i == self.urls_count:
            json = self.buildJSON()

        # print(json)

    def buildJSON(self):
        words_with_counts = self.countWords()
        final_list = []
        for word_count in words_with_counts:
            if str(word_count[1]) != '1':
                final_list.append(word_count)

        print(final_list)
        # encoded_json = json.dumps(json)
        # return encoded_json

        # json encode, and send that shit up

    def cleanWord(self, word):
        # cleaning process is not optimized, currently looking at every word and every character
        #NOTE: Next steps to improve cleaning: remove pronouns and articles, fix Retweet, its not getting removed
        clean_word = []
        chars_to_remove = [".", "'", "'s", "Retweet", ",", ":", ";", "?", "!", "-", "ed"]
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


