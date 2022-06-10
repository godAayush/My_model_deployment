import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from pprint import pprint


def do_predict(income):
    inp = pd.read_csv("D:\\8th_sem\\NLP project\\server-deploy\\flaskdemo\\demo\\housing.csv")

    X = inp["median_income"]
    Y = inp["median_house_value"]
    X = X.values.reshape(-1, 1)
    Y = Y.values

    model = LinearRegression()
    model.fit(X,Y)
    income = 8
    X_test = np.array(income)
    X_test = X_test.reshape((1,-1))
    return model.predict(X_test)

print(do_predict(8))