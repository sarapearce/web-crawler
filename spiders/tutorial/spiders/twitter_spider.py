import scrapy
import json
import csv
import pandas as pd
# from numpy import as np


class TwitterSpider(scrapy.Spider):
    name = "twitter_crawl"
    post_data = {}
    urls_count = ''
    i = 0

    def start_requests(self):
        urls = ['https://www.reddit.com/r/ProgrammerHumor/comments/92mzqt/i_always_knew_that_image_processing_was_my_strong/',"https://www.reddit.com/r/FulfillmentByAmazon/comments/92jc38/amazon_bought_one_of_my_items/","https://www.reddit.com/r/Granblue_en/comments/92bv83/progress_and_achievement_thread_july_27_2018/","https://www.reddit.com/r/piano/comments/925url/is_it_possible_to_get_to_the_point_where_you_can/","https://www.reddit.com/r/functionalprint/comments/92dxp7/modelled_and_printed_a_smartphone_hopder_for_my/", "https://www.reddit.com/r/Browns/comments/92njm0/meme_spotted_outside_the_cleveland_browns/"]


        self.urls_count = len(urls)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # currently using a counter in here as a fix for not being able to access the generators in start_requests
        # and unable to replace the yield without breaking Scrapy.
        self.i += 1
        print('Begin parsing the response')

        # grab the text of the tweet, for every tweet on the page
        # all_tweet_text = response.xpath('//*[contains(@class, "tweet-text")]/text()').extract()
        post_data = {}
        # post_data_row = {}
        # post_data_row[]
        post_data['url'] = response.url
        post_data['user'] = response.css(".doXpDd *::text").extract()
        additional_users = response.css(".JcfKy *::text").extract()

        post_time = response.css("._3jOxDPIQ0KaOWpzvSQo-1s *::text").extract()



        # print('ADDITIONAL USERS')
        # print(additional_users)
        post_data['user'].extend(additional_users)
        post_data['comment'] = response.css(".iEJDri *::text").extract()
        # post_data['post_title'] = response.css(".gVEXqn *::text").extract()
        post_data['comment_time'] = response.css(".eHkfHQ span *::text").extract()


        # print('COMMENT ARRAY LENGTH BEFORE')
        # print(len(post_data['comment']))

        if len(post_data['comment']) > len(post_data['user']):
            len_user_list = len(post_data['user'])
            len_comments_list = len(post_data['comment'])
            del post_data['comment'][len_user_list:len_comments_list]



        # print('USER ARRAY LENGTH')
        # print(len(post_data['user']))
        # print(post_data['user'])
        #
        # print('COMMENT ARRAY LENGTH AFTER')
        # print(len(post_data['comment']))
        # print(post_data['comment'])
        #
        # print('COMMENT TIME ARRAY LENGTH')
        # print(len(post_data['comment_time']))
        # print(post_data['comment'])

        print(post_data)

        df = pd.DataFrame.from_dict(post_data)
        df.to_csv('single_post_data.csv', index = False)

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
        # Next steps to improve cleaning: remove pronouns and articles, fix Retweet, its not getting removed
        clean_word = []
        chars_to_remove = [".", "'", "'s", "Retweet",
                           ",", ":", ";", "?", "!", "-", "ed"]
        for char in chars_to_remove:
            if char in word:
                clean_word = word.replace(char, '')

        cleaned_word = clean_word if clean_word else word

        return cleaned_word
    #
    # def countWords(self):
    #     distinct_words = set(self.mega_list)
    #     word_count = []
    #     for word in distinct_words:
    #         count = self.mega_list.count(word)
    #         word_count.append((word, count))
    #
    #     return word_count

    # def buildKey(self, url):
    #     date = datetime.datetime.today().strftime('%Y-%m-%d')
    #     site = url.split("/")[-1]
    #     key = site + '-' + date
    #
    #     return key
