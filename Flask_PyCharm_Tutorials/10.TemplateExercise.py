from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('TemplateExercise_index.html')

@app.route('/user')
def checkusername():
    #Set the varible that we want to use
    lower_letter = False
    upper_letter = False
    num_end = False
    user_input=request.args.get("username")
    lower_letter=any(letter.islower() for letter in user_input)
    upper_letter = any(letter.isupper() for letter in user_input)
    num_end = user_input[-1].isdigit()
    report=lower_letter and upper_letter and num_end
    return render_template('TemplateExercise_usernameCheck.html',my_input=user_input, my_lowerletter=lower_letter,
                           my_upperletter=upper_letter,my_num=num_end, my_report=report)



if __name__=="__main__":
    app.run(debug=True)