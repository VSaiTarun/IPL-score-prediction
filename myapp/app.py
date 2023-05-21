
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('linear_model.pkl','rb'))

app.debug=True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    batting_team=request.form.get('batting_team')
    bowling_team=request.form.get('bowling_team')
    overs=request.form.get('overs')
    runs=request.form.get('runs')
    wickets=request.form.get('wickets')
    runs_in_prev_5=request.form.get('runs_in_prev5_overs')
    wickets_in_prev_5=request.form.get('wickets_in_prev5_overs')

    temp_array = []
    if batting_team == 'Chennai Super Kings':
        temp_array += [1, 0, 0, 0, 0, 0, 0, 0]
    elif batting_team == 'Delhi Daredevils':
        temp_array += [0, 1, 0, 0, 0, 0, 0, 0]
    elif batting_team == 'Kings XI Punjab':
        temp_array += [0, 0, 1, 0, 0, 0, 0, 0]
    elif batting_team == 'Kolkata Knight Riders':
        temp_array += [0, 0, 0, 1, 0, 0, 0, 0]
    elif batting_team == 'Mumbai Indians':
        temp_array += [0, 0, 0, 0, 1, 0, 0, 0]
    elif batting_team == 'Rajasthan Royals':
        temp_array += [0, 0, 0, 0, 0, 1, 0, 0]
    elif batting_team == 'Royal Challengers Bangalore':
        temp_array += [0, 0, 0, 0, 0, 0, 1, 0]
    elif batting_team == 'Sunrisers Hyderabad':
        temp_array += [0, 0, 0, 0, 0, 0, 0, 1]

    if bowling_team == 'Chennai Super Kings':
        temp_array += [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowling_team == 'Delhi Daredevils':
        temp_array += [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowling_team == 'Kings XI Punjab':
        temp_array += [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowling_team == 'Kolkata Knight Riders':
        temp_array += [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowling_team == 'Mumbai Indians':
        temp_array += [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowling_team == 'Rajasthan Royals':
        temp_array += [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowling_team == 'Royal Challengers Bangalore':
        temp_array += [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowling_team == 'Sunrisers Hyderabad':
        temp_array += [0, 0, 0, 0, 0, 0, 0, 1]

    temp_array =temp_array+ [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
    temp_array = pd.to_numeric(temp_array, errors='coerce')
    temp_array = temp_array.astype(float)
    temp_array = np.array([temp_array])


    prediction=model.predict(temp_array)
    result=int(prediction[0])
    output=[result-10,result+10]
    
    
    return render_template('index.html',output=output)

if(__name__=='__main__'):
    app.run()


