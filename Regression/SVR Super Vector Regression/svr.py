#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Thai Nguyen
"""

# Regression Template

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
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)


# Fitting the SVR to the dataset
from sklearn.svm import SVR # uncommon class --> no scaling
regressor = SVR(kernel = 'rbf') # kernel = 'rbf' is non-linear
regressor.fit(X, y)

# Predict new result at level 6.5 with SVR
# since we used scaling, we need to inverse to the actual value. e.g.: 0.03 --> 1/0.03 = 33.33
# --> Use inverse transform method
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]])))) 
# single [] will be a vector, 
# a pair of bracket , [[]] become real array like matrix 
# or an array of only one line and one column that is one cell containing this 6.5 numerical value


# Visualising the SVR results
plt.scatter(X, y, color = 'red') # actually data 
plt.plot(X, regressor.predict(X), color = 'blue') 
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()



# Visualising the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1) # an vector
X_grid = X_grid.reshape((len(X_grid), 1)) # an matrix

plt.scatter(X, y, color = 'red') # actually data 
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue') 
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()



# predict new result at level 6.5 with Polynomial Regression
#lin_reg_2.predict(poly_reg.fit_transform(6.5)) 