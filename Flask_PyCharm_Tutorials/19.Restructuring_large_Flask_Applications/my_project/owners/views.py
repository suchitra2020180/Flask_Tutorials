#my_project/owners/views.py
from flask import Blueprint, render_template, redirect, url_for
from my_project import db
from my_project.models import Owner
from my_project.owners.forms import AddForm

owners_blueprints = Blueprint('owners',__name__,
                              template_folder='templates/owners')
@owners_blueprint.route('/add', methods=['GET','POST'])
def add():
   #Create forms.py first
   #Create instance of AddForm
   form=AddForm()
   if form.validate_on_submit():
       name=form.name.data
       #New a instance of puppy class, as we added a puppy name
       new_owner=Owner(name,pup_id)
       db.session.add(new_owner)
       db.session.commit()
       return redirect(url_for('list_pup'))
   return render_template('add.html', form=form)

