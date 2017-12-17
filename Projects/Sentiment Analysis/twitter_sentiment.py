import tweepy
from textblob import TextBlob
#api from twitter
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

#authorizion method
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api  = tweepy.API(auth)
#search the information about the label
public_tweets = api.search('Krishna')
#loop through the tweet
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
