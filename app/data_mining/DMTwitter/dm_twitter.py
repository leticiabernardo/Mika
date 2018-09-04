import json
import urllib.parse
import oauth2
import config
import utils.helpers as helper
from utils.tts import Tts


class DMTwitter:
    def __init__(self):
        self.tts = Tts()
        self.consumer = oauth2.Consumer(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
        self.token = oauth2.Token(config.TWITTER_TOKEN_KEY, config.TWITTER_TOKEN_SECRET)
        self.client = oauth2.Client(self.consumer, self.token)
        self.lang = "pt"

    def get_tweets(self, query='brasil'):
        query_encoded = urllib.parse.quote(query, safe='')

        request = self.client.request(
            'https://api.twitter.com/1.1/search/tweets.json?q=' + query_encoded + "&lang=" + self.lang)
        request_decoded = request[1].decode()

        twitter_object = json.loads(request_decoded)
        tweets = twitter_object['statuses']

        self.tts.speak("Os resultados de sua busca no twitter são:")

        for tweet in tweets:
            self.tts.speak(tweet['text'])
            self.tts.speak("Postado por: " + tweet['user']['screen_name'])
            self.tts.speak(helper.get_date_human_post(tweet['created_at']))

    def get_trending(self):

        request = self.client.request(
            'https://api.twitter.com/1.1/trends/place.json?id=' + str(config.YAHOO_WOE_ID) + "&lang=" + self.lang)
        request_decoded = request[1].decode()

        twitter_object = json.loads(request_decoded)
        tweets = twitter_object[0]['trends']

        self.tts.speak("Estes são os assuntos mais quentes no twitter neste momento:")

        for num, tweet in enumerate(tweets):
            self.tts.speak(tweet['name'])
            print(tweet['name'] + " | URL: " + tweet['url'])

            if num == 6:
                break

    def post_tweet(self):
        query = str(input("Novo Tweet: "))
        query_encoded = urllib.parse.quote(query, safe="")
        request = self.client.request(
            'https://api.twitter.com/1.1/statuses/update.json?status=' + query_encoded, method='POST')
        request_decoded = request[1].decode()

        twitter_object = json.loads(request_decoded)

        if twitter_object['created_at']:
            self.tts.speak("Você postou: " + twitter_object['text'] + "no twitter @" +
                           twitter_object['user']['screen_name'])
            print(twitter_object['text'] + " | por @" + twitter_object['user']['screen_name'])
