#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:33:58 2024

@author: maggielyon
"""

from sklearn.datasets import fetch_california_housing
cali = fetch_california_housing()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import random 
import pandas as pd

results = []
print('Multiple linear Regression using all features')
print('R2 Score: 0.6008983115964333')
print("MSE score: 0.5350149774449118")
cali_df = pd.DataFrame(cali.data, columns= cali.feature_names)
cali_df['MedHouseValue'] = pd.Series(cali.target)
model = LinearRegression()
for feature in cali.feature_names:
    X = cali_df[[feature]]
    y = cali_df['MedHouseValue']
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=11)
    model.fit(X=X_train, y =y_train)
    predicted = model.predict(X_test)
    expected = y_test
    df = pd.DataFrame()
    df['Expected'] = pd.Series(expected)
    df['Predicted'] = pd.Series(predicted)
    r2 = metrics.r2_score(expected,predicted)
    MSE = metrics.mean_squared_error(expected,predicted)
    print(f'{feature} has R2 score: {r2} and MSE score: {MSE}')
    results.append([feature,r2,MSE])


# +----------------+--------------+--------------+
# |   Feature      |   R2 Score   |   MSE score  |
# +----------------+--------------+--------------+
# |   MedInc       |   0.4631     |   0.7198     |
# |   HouseAge     |   0.0132     |   1.3229     |
# |   AveRooms     |   0.0241     |   1.3082     |
# |   AveBedrms    |  -0.0011     |   1.3421     |
# |   Population   |   0.0001     |   1.3404     |
# |   AveOccup     |  -0.0002     |   1.3408     |
# |   Latitude     |   0.0204     |   1.3132     |
# |   Longitude    |   0.0015     |   1.3386     |
# +----------------+--------------+--------------+
# To summarize the results of this table, it appears that median income has the greatest
# correlation with median house price, as it has the highest R2 and lowest MSE score.
# in addition, features like average bedrooms and average occuancy seem to have very
#little impact on the house price, as the r2 score is negative meaning the model is
#not a good fit at all, and the MSE scores are very high. House age, average rooms, 
# and lattitude do seem to have some effect on median cost. 

# the multiple regression example fits a much better model to the data - the R2
#and the MSE for multiple regression show a much stronger correlation between all 
# the attributes and the median cost thatn analyzing individual attributes. 


    
    