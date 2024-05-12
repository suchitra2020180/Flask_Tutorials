#############ADOPTION_SITE.PY

import os
#Here we import AddForm and DelForm from forms.py
from forms import AddForm, DelForm
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'

################
#SQL DATABASE SECTION
#########

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
#For track changes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

####### We can create this class in other model.py file.But here we created it for simplicity
##Models.py
##
class Puppy(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return f"Puppy name: {self.name}"

###################
######View functions ###have FOrms
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/Add',methods=['GET','POST'])
def add_pup():
    #Create forms.py first
    #Create instance of AddForm
    form=AddForm()
    if form.validate_on_submit():
        name=form.name.data
        #Create a new instance of puppy class, as we added a puppy name
        new_pup=Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        #list_pup is a function defined below
        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)

#creating list_pup

@app.route('/list')
def list_pup():
    #Grabing all the puppies in the database
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete',methods=['GET','POST'])
def del_pup():
    form =DelForm()
    if form.validate_on_submit():
        id=form.id.data
        #Get the puppy to be removed by id
        pup=Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)

if __name__=='__main__':
    app.run(debug=True)

