from statsmodels.tsa.stattools import adfuller
dftest = adfuller(DATA, autolag='AIC')

# P-value < 0.05 -> stationary dataset -> AutoRegressive can work
# P-value > 0.05 -> non-stationary dataset -> AutoRegressive is not suitable
print("P-Value: ", dftest[1])
