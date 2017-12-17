import tweepy
from textblob import TextBlob

consumer_key = 'qc2hFYQAFbKJZh27sxVM3oaaR'
consumer_secret = 'XZOm6eVNeWIGPQk5Oy0cmh0BIE2TcOnRtK7DVhKvsEVFqtA3Jk'

access_token = '3683057592-d0NzBcHvYA71kkiXfLB2NB15NmezBcxCeECO6RM'
access_token_secret = 'kxiKUnevd8DPhQXNNPtkgV4W7aobfkbtzG6sSznDR1Fp8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api  = tweepy.API(auth)

public_tweets = api.search('SRK')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
