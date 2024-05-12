from flask import Flask, render_template,flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'

class PuppyForm(FlaskForm):
    breed = StringField('What breed are you? ')
    submit = SubmitField('Click Me')

@app.route('/', methods=['GET','POST'])
def index():
    form=PuppyForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        flash(f"You just changed your breed to: {session['breed']}")
        return redirect(url_for('index'))

    return render_template('Forms_index.html', form=form)

if __name__=='__main__':
    app.run(debug=True)