import twitter
import json

api = twitter.Api(consumer_key='ho8YnsAGgccWm2MdOD7Yx2cOg',
              consumer_secret='SpftyunyWxnIG3ytUKo4oqLBI58Ujh2xH3SCveuS33yH0uMvjG',
              access_token_key='704797540701622273-f28XWEU3c9NTiTXo3eGedXzAh51XcWq',
              access_token_secret='FCENIOPG2fmUZijLbUH1RoMXYx6e8AreHWj8bDkNn2aEF')

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
		