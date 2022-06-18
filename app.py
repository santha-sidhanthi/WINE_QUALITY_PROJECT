# from crypt import methods
import numpy as np
from flask import Flask, redirect, render_template_string, request, jsonify, render_template, url_for
import pickle
import pandas as pd
import os
import sklearn.externals 
import joblib


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

def ValuePredictor(to_predict_list):
    to_predict=np.array(to_predict_list).reshape(1,11)
    loaded_model= pickle.load(open('model.pkl','rb'))
    result=loaded_model.predict(to_predict)
    return result[0]



@app.route('/result',methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list =request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result=ValuePredictor(to_predict_list)
        if int(result) < 6:
            p = "Poor wine to avoid!"
        else:
            p = "Nice wine to buy!"

    prediction = "This wine is classified as a {}".format(p) 
    result=round(result,2)
    s=result.astype(str)
    prediction += "   " + s + "  is its quality measure."
    
    return render_template('result.html',prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
        

