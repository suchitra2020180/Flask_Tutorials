import os.path

from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
#pip install Flask-Migrate
from flask_migrate import Migrate

#Setting SQL databse
basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'
#Set database location
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
#Tracking the changes in database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)
##############################Completed setting SQL database

Migrate(app,db)

class Table(db.Model):
    #Manual table name Choice!
    __tablename__ = 'puppies'

    id =db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    city=db.Column(db.Text)

    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    # Gives the string representation of the object
    def __repr__(self):
        return f"Person {self.name} is {self.age} year/s old"



@app.route('/', methods=['GET','POST'])
def index():
    form=website()
    if form.validate_on_submit():
        session['name']=form.name.data
        return redirect(url_for('index'))
    return render_template('base.html', form=form)

if '__name__'=='__main__':
    app.run(debug=True)