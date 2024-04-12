from flask import Flask, render_template
app =Flask(__name__)

@app.route('/')
def index():
    fruit_list=['Apple','Mango','Berry','PineApple','Water melon','Musk melon']
    return render_template('Jinja_template_Controls.html',my_list=fruit_list)

if __name__=='__main__':
    app.run(debug=True)