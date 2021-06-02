from itertools import combinations

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.feature_selection import RFE

import statsmodels.api as sm

# 2
df_raw = pd.read_csv("mianshi_2sigma/Workbook1.csv")

towns = list(df_raw.columns)
towns.remove("NYC")

ls_std = [np.std(df_raw[town]) for town in towns]
q1 = towns[np.argmax(ls_std)]

rows_wanted = (df_raw["B"] >= 60) & (df_raw["B"] <= 70)

q2 = np.median(df_raw.loc[rows_wanted, "NYC"])

ls_mse = []
sum_beta = 0

for town in towns:
    X = df_raw[town].values.reshape(-1, 1)
    Y = df_raw["NYC"].values.reshape(-1, 1)
    reg = LinearRegression(fit_intercept=True).fit(X=X, y=Y)
    intercept = reg.intercept_[0]
    beta = reg.coef_[0][0]
    mse = mean_squared_error(y_true=Y, y_pred=reg.predict(X=X))
    # XX = sm.add_constant(X)
    # mod = sm.OLS(endog=Y, exog=XX)
    # mod.fit().summary()
    sum_beta += np.abs(beta)
    ls_mse.append(mse)

q3 = sum_beta
q4 = towns[np.argmin(ls_mse)]

town_pairs = list(combinations(towns, 2))

ls_mse_2 = []
for town_pair in town_pairs:
    X = df_raw[list(town_pair)].values
    Y = df_raw["NYC"].values.reshape(-1, 1)
    reg = LinearRegression(fit_intercept=True).fit(X=X, y=Y)
    intercept = reg.intercept_[0]
    beta = reg.coef_[0]
    mse = mean_squared_error(y_true=Y, y_pred=reg.predict(X=X))
    ls_mse_2.append(mse)

q5 = town_pairs[np.argmin(ls_mse_2)]

# 3
# backward or forward selection .
X = df_raw[towns].values
Y = df_raw["NYC"].values.reshape(-1, 1)

reg = LinearRegression(fit_intercept=True)
selector = RFE(reg, n_features_to_select=5, step=1)
selector = selector.fit(X=X, y=Y)
support = selector.support_
ranking = selector.ranking_

towns_5 = np.array(towns)[support]
q3 = towns_5