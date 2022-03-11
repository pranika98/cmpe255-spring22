import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

class CarPrice:

    def __init__(self):
        self.df = pd.read_csv('data/data.csv')
        print(f'${len(self.df)} lines loaded')

    def trim(self):
        self.df.columns = self.df.columns.str.lower().str.replace(' ', '_')
        string_columns = list(self.df.dtypes[self.df.dtypes == 'object'].index)
        for col in string_columns:
            self.df[col] = self.df[col].str.lower().str.replace(' ', '_')

    # This function will check the rmse value between the inputted observed and predicted sets
    def validate(self, y_train, y_pred):
        error = y_pred - y_train
        rmse = (error ** 2).mean()
        ans = np.sqrt(rmse)
        return ans
        
    # Get the linear regression parameters based on the training set
    def linear_regression(self, x, y):
        ones = np.ones(x.shape[0])
        x = np.column_stack([ones, X]) #Apply a column of 1s to get bias term
        xTranspose = x.T.dot(X)
        xTranspose_inv = np.linalg.inv(xTranspose)
        w = xTranspose_inv.dot(x.T).dot(y) #Formula to get the array of weight parameters
        return w[0], w[1:] #First term is the bias term, and afterwards is the weights for each feature
        