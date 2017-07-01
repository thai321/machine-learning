#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Thai Nguyen
"""

# Multiple Linear Regression
# Method: Backward Elimination

# Importing the libararies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#np.set_printoptions(threshold = np.nan)

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values # Take all the columns's values except the last one
y = dataset.iloc[:, 4].values # take a last column' values, purchase column

# Encoding categorical Data
# Encoding the Independent variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3]) # the States
onehotencoder = OneHotEncoder(categorical_features=[3]) # first column be categoried
X = onehotencoder.fit_transform(X).toarray()


# Avoiding the Dummy Variable Trap
X = X[:, 1:] # get rid of the 1st column value (a state of California)


# ********** Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)
# There are 50 observations in the data, we will have 10 in the test set and 40 in the train set


# ********** Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Fittin gMultiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)


#  ********** Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X , axis = 1)
# 50 lines and 1 column. If want to add to line, then axis = 0; add to column then axis = 1

# Step 1: Select a significance level to stay in the model (e.g. >SL = 0.05)
X_opt = X[:, [0,1,2,3,4,5]] # set X optimal to origin maxtrix X

# Step 2: Fit the full model with all possible predictors
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()  # OLS object

# Step 3: Consider the predictor with the highest P-value.
# If P > SL, go to Step 4, otherwise go to FIN (Your Model is >Ready)
regressor_OLS.summary() # a Table


X_opt = X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary() 

X_opt = X[:, [0,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary() 

X_opt = X[:, [0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary() 

X_opt = X[:, [0,3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary() 