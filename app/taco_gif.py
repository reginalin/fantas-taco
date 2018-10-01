import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import json

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'rP4mJuAPvjwuhogUGvMQc8Fbbfr3TraD' # str | Giphy API Key.

def get_gif_json(tag):
	rating = 'g' # str | Filters results by specified rating. (optional)
	fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
	try: 
	    # Random Sticker Endpoint
	    api_response = api_instance.stickers_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
	    return api_response
	    
	except ApiException as e:
	    print("Exception when calling DefaultApi->stickers_random_get: %s\n" % e)

def get_gif_url(tag):
	gif = get_gif_json(tag).data
	url = gif.fixed_height_downsampled_url
	return url