# Owners folder====> forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name=StringField('Name of the Owner:')
    pup_id=IntegerField("Id of te Puppy:")
    submit=SubmitField('Add owner')
