# Polynominal Regression
# Predict the salary at level 10

# Importing the libararies 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#np.set_printoptions(threshold = np.nan)

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values # consider to be maxtrix( not vector) even though it has 1 column values
y = dataset.iloc[:, 2].values # take a last column' values, purchase column. Consider to be a vector

# No need to split to data sets since we only have 10 observations --> not need for train
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


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

# Fittin Polynomiial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4) # change to 2, 3, 4
X_poly = poly_reg.fit_transform(X) 
lin_reg_2 = LinearRegression() 
lin_reg_2.fit(X_poly, y) # building a linear polynomial regression 

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'red') # actually data (salary)
plt.plot(X, lin_reg.predict(X), color = 'blue') # predict the level 10
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()


# Visualising the Polynomial Regression results
X_grid = np.arange(min(X), max(X), 0.1) # an vector
X_grid = X_grid.reshape((len(X_grid), 1)) # an matrix

plt.scatter(X, y, color = 'red') # actually data (salary)
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue') # predict the level 10
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position label')
plt.ylabel('Salary')
plt.show()


# Predict new result at level 6.5 with Linear Regression
lin_reg.predict(6.5) # ~ 330,378

# predict new result at level 6.5 with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5)) # 158,862 --> better