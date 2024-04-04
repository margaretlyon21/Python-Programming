#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:24:13 2024

@author: maggielyon
"""
import pandas as pd

"""
+----------------------+-------------------+
| Number of Estimators | Model Accuracy (%)|
+----------------------+-------------------+
|          1           |       67.21       |
|          2           |       73.77       |
|          3           |       73.77       |
|          4           |       72.13       |
|          5           |       77.05       |
|          6           |       78.69       |
|          7           |       85.25       |
|          8           |       80.33       |
|          9           |       86.89       |
+----------------------+-------------------+
"""

import pandas as pd
import numpy as np
# Modify this to your file system
heart_disease = pd.read_csv('heart.csv') 
X = heart_disease.drop(['target'] , axis=1) 
Y = heart_disease['target']
from sklearn.ensemble import RandomForestClassifier 
clf = RandomForestClassifier(n_estimators=1)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)                                                
clf.fit(X_train, Y_train)
y_pred = clf.predict(X_test)
print(clf.score(X_train, Y_train))
print(clf.score(X_test, Y_test))


np.random.seed()
for i in range(1,10,1):
        print(f"trying model with {i} estimators")
        clf = RandomForestClassifier(n_estimators = i).fit(X_train,Y_train)
        print(f"Model accuracy on test set: {clf.score(X_test, Y_test)*100:.2f}%")
        print(" ")
# My Output
# 0.987603305785124
# 0.8524590163934426