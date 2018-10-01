import twitter
import json
from app import app

api = twitter.Api(consumer_key=app.config['CONSUMER_KEY'],
              consumer_secret=app.config['CONSUMER_SECRET'],
              access_token_key=app.config['ACCESS_TOKEN_KEY'],
              access_token_secret=app.config['ACCESS_TOKEN_SECRET'])

def get_tweets():
	stream = tweet_stream()
	text = filter_tweets(stream)
	return text

# tweet stream of taco hashtag
def tweet_stream():
	raw_query = "q=%23tacos%20&result_type=recent&count=100"
	return api.GetSearch(raw_query=raw_query)

# return list of tweet texts only
def filter_tweets(stream):
	filtered_text = []
	for tweet in stream:
		text = tweet._json["text"]
		filtered_text.append(text)
	return filtered_text
		