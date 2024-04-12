from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Welcome! Go to /puppy_latin/name to see your name in latin </h1>'

@app.route('/puppy_latin/<name>')
def Latin_puppy(name):
    if name[-1] != 'y':
        name=name+'y'
    else:
        name=name[0:-1]+'iful'
    return '<h1> Your puppy latin name is {}</h1>'.format(name)

if __name__=='__main__':
    app.run(debug=True)