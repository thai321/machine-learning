# Regressions

## Simple Linear Regressions:

  > `y = b_0 + b_1 * x_1`

- Dependent variable (DV) : y
- Idependent variable (IV) : X_1
- Coefficient : b_1
- Constant term : b_0

### Ordinary Least Square:
> `Sum(y-y^)^2  -> min`
- y^ is the value on the model line, y is actual value

***

## Multiple Linear Regressions
> `y = b_0 + b_1 * x_1 + b_2 * x_2 + ... +b_n * x_n`

- Dependent variable (DV) : y
- Independent variables (IVs) : x_1, x_2, x_n
- Coefficients : b_1, b_2, b_n
- Constant term : b_0

### 5 methods building a model
1. All-in : throw all your variables
  >+ Prior knowledge; OR
  >+ You have to; OR
  >+ Preparing for Backward Elimination

2. Backward Elimination
  >+ Step 1: Select a significance level to stay in the model (e.g. >SL = 0.05)
  >+ Step 2: Fit the full model with all possible predictors
  >+ Step 3: Consider the predictor with the highest P-value.
  If P > SL, go to Step 4, otherwise go to FIN (Your Model is >Ready)
  >+ Step 4: Remove the predictor
  >+ Step 5: Fit model without this variable* --> Step 3

3. Forward selection
4. Bidirectional Elimination
5. All Possible Model
