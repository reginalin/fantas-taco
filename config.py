import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-secret-key-supposed-to-be-here'

    # Giphy API Key.
    GIPHY_API_KEY = 'rP4mJuAPvjwuhogUGvMQc8Fbbfr3TraD' 

    # Twitter API keys
    CONSUMER_KEY = 'ho8YnsAGgccWm2MdOD7Yx2cOg'
    CONSUMER_SECRET = 'SpftyunyWxnIG3ytUKo4oqLBI58Ujh2xH3SCveuS33yH0uMvjG'
    ACCESS_TOKEN_KEY = '704797540701622273-f28XWEU3c9NTiTXo3eGedXzAh51XcWq'
    ACCESS_TOKEN_SECRET = 'FCENIOPG2fmUZijLbUH1RoMXYx6e8AreHWj8bDkNn2aEF'


