from flask import Flask, render_template, flash, session,redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
#Configure a secret key for securiy work, the security key is built in flask applications
app.config['SECRET_KEY']='mykey'

#Creating a form
class SimpleForm(FlaskForm):
    submit=SubmitField('Click Me') #Submit button

@app.route('/',methods=['GET','POST'])
def index():
    #Create instance of a class
    form =SimpleForm()
    #Check logic
    if form.validate_on_submit(): #then grab the data
        #flash message
        flash('You just clicked the button!!')
        return redirect(url_for('index'))

    return render_template('Flash_index.html', form=form)

if __name__=='__main__':
    app.run(debug=True)
