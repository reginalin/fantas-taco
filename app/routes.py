from flask import render_template
from app import app
from app.forms import RandomForm

@app.route('/')
@app.route('/index')
def index():
	form = RandomForm()
	return render_template('index.html', title='Home', form=form)