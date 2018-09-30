from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#realy just a button that when submitted calls a random function to decide
class RandomForm(FlaskForm):
    submit = SubmitField('Decide')