#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Thai Nguyen
"""

# Decision Tree Regression

# Importing the libararies 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#np.set_printoptions(threshold = np.nan)

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values # consider to be maxtrix( not vector) even though it has 1 column values
y = dataset.iloc[:, 2].values # take a last column' values, purchase column. Consider to be a vector

# If you have enough data set, the use it
# ********** Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 1/3, random_state = 0)"""
# There are 30 observations in the data, we will have 10 in the test set and 20 in the train set

# No need to apply feature scalling
# ********** Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


# Fitting the Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

# Predict new result at level 6.5 with the Regression
y_pred = regressor.predict(6.5) 


# Visualising the Decision Tree Regression results
plt.scatter(X, y, color = 'red') # actually data 
plt.plot(X, regressor.predict(X), color = 'blue') 
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()



# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
# refer for non-continuum model
X_grid = np.arange(min(X), max(X), 0.01) # an vector
X_grid = X_grid.reshape((len(X_grid), 1)) # an matrix

plt.scatter(X, y, color = 'red') # actually data 
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue') 
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()


