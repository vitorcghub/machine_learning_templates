# -*- coding: utf-8 -*-
"""multiple_linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16GHkS_Ce5FXhda1rdJQu3vocbcpRlq5b

# Multiple Linear Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

"""## Encoding categorical data"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

print(X)

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

"""## Training the Multiple Linear Regression model on the Training set"""

#vamos usar uma classe que automaticamente escolhe as melhores variaveis independentes (sem necessidade de usar backward elimination)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression() 
regressor.fit(X_train, y_train)

"""## Predicting the Test set results"""

#vamos criar dois vetores que comparam os resultados previstos com os reais do test set
y_pred = regressor.predict(X_test)
np.set_printoptions(precision = 2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_pred), 1)), 1)) #usamos o metodo de concatenar para juntar os dois vetores. Reshape serve para mostra-los na vertical.