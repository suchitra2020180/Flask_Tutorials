from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home1.html')

@app.route('/signup')
def Signing():
    return render_template('SignUp.html')

@app.route('/thanking')
def thankyou():
    # Grab the first and last name provided by the user using "request" module
    first=request.args.get('fname')
    last = request.args.get('lname')
    return render_template('thanks.html', my_first=first, my_last=last)

if __name__=='__main__':
    app.run(debug=True)