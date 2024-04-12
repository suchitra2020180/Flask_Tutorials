from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    #Some code
    user_logged_in=True
    return render_template('jinja_template_userlogin.html', my_login=user_logged_in)

if __name__=='__main__':
    app.run(debug=True)