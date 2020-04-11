from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField
from flask_bootstrap import Bootstrap
import GPA_Prediction_Using_Two_File_Dataset

# App config.
DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'
 
class NameForm(Form):
    sat_score = TextField('SAT Score:')
 
@app.route("/", methods=['GET', 'POST'])
def cgpaPrediction():
    form = NameForm(request.form)

    if request.method == 'POST':
        sat_score = request.form['sat_score']
        sat_score = GPA_Prediction_Using_Two_File_Dataset.prediction(float(sat_score))

        flash('CGPA = ' + str(sat_score) )
         
    return render_template('index.html', form=form)
