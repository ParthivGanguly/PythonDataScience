import tweepy
from textblob import TextBlob
import csv

myFile = open('twitter_sentiment.csv', 'w')
sentiments = [['Tweet', 'Sentiment']]

consumer_key = '5jFdQPbGtWkz31vXl0HQW4WPk'
consumer_secret = 'w8JFsbFsvl4K0hh5xXqssAu8S87wTe0SNEVq1r9RPfP0VUNmhS'

access_token = '971375935940386816-adY0Y2rwvfdMwh4YvbrZsDA0Jz3HFp1'
access_token_secret = 'mIZrzhggUbmuGCE656QCHOqY6PpnqO6Nf0ChwjjDTyHfR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
  print(tweet.text)
  analysis = TextBlob(tweet.text)
  print(analysis.sentiment)
  if analysis.sentiment.polarity > 0:
    sentiment = 'positive'
  elif analysis.sentiment.polarity < 0:
    sentiment = 'negative'
  else:
    sentiment = 'neutral'
  sentiments.append([tweet.text, sentiment])

with myFile:
  writer = csv.writer(myFile)
  writer.writerows(sentiments)