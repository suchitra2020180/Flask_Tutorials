#my_project/owners/views.py
from flask import Blueprint, render_template, redirect, url_for
from my_project import db
from my_project.models import Puppy
from my_project.puppies.forms import AddForm, DelForm

owners_blueprints = Blueprint('puppies',__name__,
                              template_folder='templates/puppies')
@puppies_blueprint.route('/add', methods=['GET','POST'])
def add():
   #Create forms.py first
   #Create instance of AddForm
   form=AddForm()
   if form.validate_on_submit():
       name=form.name.data
       #New a instance of puppy class, as we added a puppy name
       new_pup=Owner(name)
       db.session.add(new_pup)
       db.session.commit()
       return redirect(url_for('list_pup'))
   return render_template('add.html', form=form)

#creating list_pup


@puppies_blueprint.route('/list')
def list_pup():
   #Grabing all the puppies in the database
   puppies = Puppy.query.all()
   return render_template('list.html', puppies=puppies)

@puppies_blueprint.route('/delete',methods=['GET','POST'])
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