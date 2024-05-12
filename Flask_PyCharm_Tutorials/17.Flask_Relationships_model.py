#MODEL.PY
import os
from flask import Flask, render_template, redirect, url_for()
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'
#Set database location
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
#Tracking the changes in database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):
    __tablenmae__='puppies'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    #ONE TO MANY
    #Puppy to many toys
    toys=db.relationship('Toy',backref='puppy',lazy='dynamic')
     # ONE TO ONE
    #Puppy to ONe Owner
    owner=db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self.name):
        self.name=name
    def __repr__(self):
        if self.owner:  #If the puppy has owner
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet!!"
    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    __tablename__='toys'
    id=db.Column(db.Integer,primary_key=True)
    item_name=db.Columns(db.Text)
    puppy_id=db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self,item_name,puppy_id):
        self.item_name =item_name
        self.puppy_id=puppy_id


class Owner(db.Model):
    __tablename__='owners'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)

    puppy_id=db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
       self.name=name
       self.puppy_id=puppy_id


if __name__=='__main__':
    app.run(debug=True)