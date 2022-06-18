# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df=pd.read_csv('Data/winequality-red.csv')

y = df['quality']
x = df.drop(['quality'],axis=1)

#Splitting Training and Test Set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()


#Fitting model with trainig data
regressor.fit(x_train, y_train)
prediction_test=regressor.predict(x_test)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[0.5,0.9,3,5,1,2,.2,.8,.9,4,9]]))