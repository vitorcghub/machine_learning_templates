# -*- coding: utf-8 -*-
"""polynomial_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CdAW_eT1h7dnFGd0Sg76E2fty9gjv98p

# Polynomial Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

"""## Training the Linear Regression model on the whole dataset"""

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y) #nao eh necessario separar em test e training set

"""## Training the Polynomial Regression model on the whole dataset"""

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X) #criando a matriz de features ao quadrado
lin_reg_2 = LinearRegression() #estamos adicionando a matriz de features ao quadrado ao modelo linear, pois vamos ajustar y = a + bx + cx^2
lin_reg_2.fit(X_poly, y)

"""## Visualising the Linear Regression results"""

plt.scatter(X, y, color = 'red') #plotando os pontos do dataset
plt.plot(X, lin_reg.predict(X), color = 'blue') #plotando a linha de regressao linear
plt.title('Truth or Bluff (linear regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

"""## Visualising the Polynomial Regression results"""

plt.scatter(X, y, color = 'red') #plotando os pontos do dataset
plt.plot(X, lin_reg_2.predict(X_poly), color = 'blue') #plotando a linha de regressao linear
plt.title('Truth or Bluff (polynomial regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

"""## Training the Polynomial Regression with degree = 4"""

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X) #criando a matriz de features ao quadrado
lin_reg_2 = LinearRegression() #estamos adicionando a matriz de features ao quadrado ao modelo linear, pois vamos ajustar y = a + bx + cx^2
lin_reg_2.fit(X_poly, y)

"""## Visualising the Polynomial Regression results (for higher resolution and smoother curve)"""

X_grid = np.arange(min(X), max(X), 0.1) #separando em passos menores para ficar mais suave
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red') 
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue') #plotando a linha de regressao linear
plt.title('Truth or Bluff (polynomial regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

"""## Predicting a new result with Linear Regression"""

lin_reg.predict([[6.5]]) #arrays tem 2 pares de colchetes

"""## Predicting a new result with Polynomial Regression"""

lin_reg_2.predict(poly_reg.fit_transform([[6.5]])) #nao podemos colocar apenas 6.5, mas tbm 6.5^2, 6.5^3 e 6.5^4. Por isso usamos o poly_reg.fit_transform