# from crypt import methods
import numpy as np
from flask import Flask, redirect, request, jsonify, render_template, url_for
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')


# @app.route('/predict', methods = ['POST', 'GET'])
# def predict():
#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#     #print(prediction[0])

#     #return prediction[0]

#     output = round(prediction[0], 2)
#     return render_template('predict.html', prediction_text=output)

@app.route('/predict' , methods=['POST', 'GET'])
def predict():
    fixed_acidity = request.form['fixedAcidity']
    volatile_acidity = request.form['volatileAcidity']
    citric_acid = request.form['citricAcid']
    residual_sugar = request.form['residualSugar']
    chlorides =  request.form['chlorides']
    free_sulfur_dioxide =  request.form['freeSulfurDioxide']
    total_sulfur_dioxide = request.form['totalSulfurDioxide']
    density = request.form['density']
    pH =  request.form['pH']
    sulphates = request.form['sulphates']
    alcohol = request.form['alcohol']


        # create a dataframe to store inputs for prediction
    wine_df = pd.DataFrame(columns=["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
                                        "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide",
                                        "density", "pH", "sulphates", "alcohol"])



    wine_df.loc[0] = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,
                          total_sulfur_dioxide,density,pH,sulphates,alcohol]


    #     # change datatype from object to float
    # wine_df = wine_df.astype("float")

    pred_quality = model.predict(wine_df)
    pred_quality_num = pred_quality[0]


        # logger.info("prediction made: {:0.3f}".format(pred_quality_num))
    evaluation=""    

    if pred_quality_num >= 5:
        evaluation = "Nice wine to buy!"
    elif pred_quality_num < 5:
        evaluation = "Poor wine to avoid!"

        

    prediction_text = "This wine is classified as a {}".format(evaluation) 

    s=pred_quality[0].astype(str)

    prediction_text += "   " + s + "  is its quality measure."

    return render_template('predict.html', prediction_text=prediction_text)




@app.route('/predict_api/',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)







if __name__ == '__main__':
    app.run(debug=True)    

