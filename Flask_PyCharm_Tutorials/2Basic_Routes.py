from flask import Flask
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return '<h1> Hello World </h1>'

@app.route('/MyProfile') #127.0.0.1:5000/MyProfile
def profile():
    return '<h1> I am Suchitra </h1>'

#Dynamic Routing
#Here <name> is a variable
@app.route('/MyPage/<name>')
def mypage(name):
    return '<h1> Hello {}. This is your page</h1>'.format(name)


#Converting the given name into upper case
@app.route('/MyName/<name>')
def myName(name):
    return '<h1> Upper case of given name is  {}</h1>'.format(name.upper())
#To find the 100th letter of the given name
#If the given name does not have 100 letters then it will return internal server error
@app.route('MyCount/<name>')
def mycount(name):
    return '<h1> 100th letter of the name: {} </h1>'.format(name[100])

if __name__=='__main__':
    app.run()