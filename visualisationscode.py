import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#ALternative, better use of the function
def analysis2(tickers, start, end, period): 
    pdata = yf.download(tickers, start, end, period)
    pdata = pdata.iloc[:,:2]

    pdata.columns = ["SPY", "TNX"]
    
    #drop NAs columns 
    pdata = pdata.dropna()
    
    return pdata

pdata = analysis2(["SPY", "^TNX"], "2000-01-01", "2022-01-01", 'ld')
print(pdata)

#Display BASIC scatter plot and deciled scatter 

fig, [ax1, ax2] = plt.subplots(1, 2, figsize=[15,6])
pdata.plot.scatter(x="SPY",
                   y="TNX", 
                   title="Interest Rate vs Stock market rate return",
                   ax=ax1, 
                   alpha=0.5,
                   c="blue")#alpha change de density of the point so we see more clearly

#denition of the deciled variable
plotdata = pdata[["SPY","TNX"]].groupby(pd.qcut(pdata["SPY"],10)).mean()

#visualisation of the deciled variable
plotdata.plot.scatter(x="SPY",
                      y="TNX",
                      title="Tinterest Rate Vs Stock market rate return (deciled)",
                      xlabel="Stock market return",
                      ylabel="Interest rate",
                      ax=ax2,
                      c="r")

ax1.grid(ls="--")
ax2.grid(ls="--")

plt.show()

#LINEAR REGRESSION
from sklearn.linear_model import LinearRegression

#definition of variable x and y
X_ = np.array(pdata["SPY"]).reshape(-1,1)
Y_ = np.array(pdata["TNX"]).reshape(-1,1)

model = LinearRegression()
model.fit(X_, Y_) 
prediction = model.predict(X_) #prediction 
score = model.score(X_, Y_) #Coefficient of Determination

#visualisation 
fig, ax = plt.subplots(figsize=[8,5], dpi=130)
ax.scatter(X_, Y_, alpha=0.5, label="data")
ax.plot(X_, prediction, c="red", label="regression line")

#title and labels
ax.set(title="Linear Regression", ylabel="TNX", xlabel="SPY")

ax.grid(ls="--")
plt.legend() #allow to show the labels


plt.show()

#Score of Linear Regression for raw data
print(f"Coefficient of Determination : {score:.4f}") #:.4f allow to modify the numbers after the comma

#Equation of regression:
coef = model.coef_ #Estimated coefficients for the linear regression problem
intercept = model.intercept_ #Independent term
print(f"Equation of regression : Y = {float(intercept):.3f} + ({float(coef):.3f}) * x")

#POLYNOMIAL REGRESSION
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

#Use of loop to try different degree
for i in range(2,10): 
    poly_reg = PolynomialFeatures(degree=i)
    X_poly = poly_reg.fit_transform(X_)

    model_poly = LinearRegression()
    model_poly.fit(X_poly, Y_)

    Y_poly_prediction = model_poly.predict(X_poly)
    
    fig, ax = plt.subplots(figsize=[5,5],dpi=150)
    ax.scatter(X_, Y_, alpha=0.5, label="data")
    ax.plot(X_, Y_poly_prediction, c="r")
    
    r2_poly = r2_score(Y_, Y_poly_prediction)
    print(f"R2 score : {r2_poly:.4f} for degree {i}")
    
    ax.grid(ls="--")
    
    plt.show()



