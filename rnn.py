# Recurrent Neural Network
# Part 1 - Data preprocessing

# CS 229 Stanford 
# http://cs229.stanford.edu/proj2012/BernalFokPidaparthi-FinancialMarketTimeSeriesPredictionwithRecurrentNeural.pdf
# train LSTM on five years of Google 
# Supervised Deep Learning

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the training set
training_set = pd.read_csv("Google_Stock_Price_Train.csv")

# input/ouputs of recurrent neural (input != date, stock price)
# but stock price at time t for input, and stock price t+1 for the output
# create a set only with the "Open" Google stock price, extract that column
# two-dimensional numpy array
training_set = training_set.iloc[:,1:2].values

# Feature Scaling + Normalization, since LSTM Several Sigmoid Activation function
# Sigmoid 0 and 1, as is the case in Normalization
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler() # default is 0,1
# Fitting to training_set, scale training set, 
# transform we'll apply normalizationjust need min and max for normalization
training_set = sc.fit_transform(training_set)