from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import RandomForm
from app import decide, taco_tweets, taco_gif

@app.route('/', methods=['GET', 'POST'])
def index():
	form = RandomForm()
	if form.validate_on_submit():
		flash(decide.randomDecision())
		return redirect(url_for('index'))
	return render_template('index.html', title='Home', form=form)

@app.route('/tweets')
def tweets():
	tweet_stream = taco_tweets.get_tweets()
	return render_template('tweets.html', title='Taco Tweets', taco_tweets=tweet_stream)

@app.route('/gif')
def gif():
	url = taco_gif.get_gif_url('taco')
	return render_template('gif.html', title='Taco Gif', url=url)