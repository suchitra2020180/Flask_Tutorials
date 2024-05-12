from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, RadioField, SelectField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'

class formtypes(FlaskForm):
    name=StringField('Enter your name:',validators=[DataRequired()])
    Agreed=BooleanField('Have to agreed to fill the form?')
    mood=RadioField('Choose your mood:', choices=[('mood_one','Happy'),('mood_two','Sad')])
    Food_choice=SelectField(u'Pick your favourite food:',choices=[('chi','Chicken'),('fh','Fish')])
    Feedback=TextAreaField()
    submit=SubmitField('Submit Details')

@app.route('/',methods=['GET','POST'])
def index():
    form=formtypes()
    if form.validate_on_submit():
        session['name']=form.name.data
        session['Agreed']=form.Agreed.data
        session['mood']=form.mood.data
        session['food']=form.Food_choice.data
        session['feedback']=form.Feedback.data
        return redirect(url_for('Df_FlaskForms_thankyou'))
    return render_template('Df_FlaskForms_index.html',form=form)

@app.route('/Df_FlaskForms_thankyou')
def Df_FlaskForms_thankyou():
    return render_template('Df_FlaskForms_thankyou.html')

if __name__=='__main__':
    app.run(debug=True)
