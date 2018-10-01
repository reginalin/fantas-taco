import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'rP4mJuAPvjwuhogUGvMQc8Fbbfr3TraD' # str | Giphy API Key.
# tag = 'burrito' # str | Filters results by specified tag. (optional)
rating = 'g' # str | Filters results by specified rating. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

def get_gif(tag):
	try: 
	    # Random Sticker Endpoint
	    api_response = api_instance.stickers_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
	    pprint(api_response)
	except ApiException as e:
	    print("Exception when calling DefaultApi->stickers_random_get: %s\n" % e)