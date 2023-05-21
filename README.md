# First Innings IPL Score Prediction

This project uses machine learning techniques to predict the first innings score in IPL matches. It provides a web interface where users can input the details of the ongoing match, such as the batting team, bowling team, overs played, runs scored, wickets taken, runs scored in the last 5 overs, and wickets taken in the last 5 overs. Based on this information, the model predicts the score range for the first innings.

## Prerequisites

- Python 3.6 or higher
- Flask web framework
- scikit-learn library
- NumPy and pandas libraries
- Pickle library

## Running Flask application
First create a virtual environment "myenv" to store our flask application.

Upon creating virtual environment activate that environment using myenv\scripts\activate and then run your python file using python app.py command

1. Open a web browser and go to `http://localhost:5000` to access the application.

2. Enter the details of the ongoing match in the provided form.

3. Click the "Submit" button to get the predicted score range for the first innings.

## Model Training

The machine learning model used for score prediction is trained using historical IPL match data. 
The training process involves preprocessing the data, such as one-hot encoding the categorical variables and scaling the numerical variables. 
The model is then trained using a regression algorithm.
The trained model is saved as a pickle file (`linear_model.pkl`) and loaded during the application runtime for making predictions.

## Refrence
https://www.section.io/engineering-education/deploying-machine-learning-models-using-flask/

### Sample Input and Output

> Input
<img width="500" alt="image" src="https://github.com/VSaiTarun/IPL-score-prediction/assets/132877695/8ffb6e9d-4bbc-4b92-879a-f3172b72db79">

>output

<img width="500" alt="image" src="https://github.com/VSaiTarun/IPL-score-prediction/assets/132877695/02624631-1964-4c41-9934-efb43ba9a9d1">
















