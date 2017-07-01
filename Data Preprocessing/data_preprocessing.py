#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ThaiNguyen
"""
# Importing the libararies 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#np.set_printoptions(threshold = np.nan)

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values # Take all the columns's values except the last one
y = dataset.iloc[:, 3].values # take a last column' values, purchase column

# ********** Missing Data processing
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0) # replace the missing value with the mean values
imputer = imputer.fit(X[:, 1:3]) # take columns 1 and 2 's values
X[:, 1:3] = imputer.transform(X[:, 1:3]) 


# Encoding categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

onehotencoder = OneHotEncoder(categorical_features=[0]) # first column be categoried
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# ********** Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0) 
# there are 10 observations in the data, we will have 2 in the test set and 8 in the train set


# ********** Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
