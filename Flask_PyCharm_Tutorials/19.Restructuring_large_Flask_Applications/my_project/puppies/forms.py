from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
   name=StringField('Name of the Puppy: ')
   submit=SubmitField('Add Puppy')


class DelForm(FlaskForm):
   #Since puppies can have same names, we will remove puppies by their id
   id=IntegerField("Id number of Puppy to remove from database:")
   submit = SubmitField("remove Puppy")
