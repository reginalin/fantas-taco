from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#really just a button
class RandomForm(FlaskForm):
    submit = SubmitField('click to decide')

class GifForm(FlaskForm):
	submit = SubmitField('new gif')