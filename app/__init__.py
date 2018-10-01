from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    app.debug = True
    app.run()

from app import routes