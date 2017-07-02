# Regressions

## Simple Linear Regressions:

  > `y = b0 + b1 * x1`

- Dependent variable (DV) : y
- Idependent variable (IV) : X1
- Coefficient : b1
- Constant term : b0

### Ordinary Least Square:
> `Sum(y-y^)^2  -> min`
- y^ is the value on the model line, y is actual value

***

## Multiple Linear Regressions
> `y = b0 + b1 * x1 + b2 * x2 + ... +bn * xn`

- Dependent variable (DV) : y
- Independent variables (IVs) : x1, x2, xn
- Coefficients : b1, b2, bn
- Constant term : b0

### 5 methods building a model
1. All-in : throw all your variables
  >+ Prior knowledge; OR
  >+ You have to; OR
  >+ Preparing for Backward Elimination

2. Backward Elimination
  >+ `Step 1`: Select a significance level to stay in the model (e.g. >SL = 0.05)
  >+ `Step 2`: Fit the full model with all possible predictors
  >+ `Step 3`: Consider the predictor with the highest P-value.
  If P > SL, go to `Step 4`, otherwise go to FIN (Your Model is >Ready)
  >+ `Step 4`: Remove the predictor
  >+ `Step 5`: Fit model without this variable* --> `Step 3`

3. Forward selection
4. Bidirectional Elimination
5. All Possible Model

## Polynomial Linear Regression
> `y = b0 + b1 * x1 + b2 * (x1)^2 + ... + bn * (x1)^n`

## Radom Forest Intutition
+ Ensemble Learning: random forest is a version of ensemble learning.
It is when you take multiple algorithms or the same algorithm multiple times, and put them together.

> + `Step 1`: Pick at random K data points from the Training set
> + `Step 2`:Build the Decision Tree associated to these K data points
> + `Step 3`: Choose the number Ntree of trees you want to build and repeat Steps 1 & 2
> + `Step 4`: For a new data point, make each one of your Ntree trees predict the value of Y
to for the data point in question, and assign the new data point the average across all of the predicted Y values
