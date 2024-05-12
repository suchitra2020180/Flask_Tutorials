
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
#Configure a secret key for securiy work, the security key is built in flask applications
app.config['SECRET_KEY']='mysecretkey'

#Creating a form
class InfoForm(FlaskForm):
    # Here we want to know about puppy
    # Here breed is an attribute
    # <!--- To use label,input of text type in forms we will use StringField--->
    breed=StringField("What Breed are you?")
    submit=SubmitField('Submit') #Submit button

@app.route('/',methods=['GET','POST'])
def index():
    #Here breed is an variable
    breed = False
    #Create instance of a class
    form =InfoForm()
    #Check logic
    if form.validate_on_submit(): #then grab the data
        breed = form.breed.data
        form.breed.data=''
    return render_template('FormBasics_index.html', form=form, breed=breed)

if __name__=='__main__':
    app.run(debug=True)
