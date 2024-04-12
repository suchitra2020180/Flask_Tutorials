from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    some_variable='Suchitra'
    letters=list(some_variable)
    fruit_dict={'Fruit_name':'Apple'}
    list=[1,2,3,4,5,6,7,8]
    return render_template('jinja_basic.html', my_variable=some_variable,
                           my_letters=letters, my_dictionary=fruit_dict,my_list=list)

if __name__ == '__main__':
    app.run(debug=True)