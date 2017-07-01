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

# Missing Data processing
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

onehotencoder = OneHotEncoder(categorical_features=[0]) # first column be categoried
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)