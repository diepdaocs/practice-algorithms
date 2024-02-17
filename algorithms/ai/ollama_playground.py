######################## AI generated code, yet to test ######################################
# Write a python model to predict real estate price
# using keras library.
# 1) Download or get the data
# 2) Data preprocessing
# 3) Building the neural network
# 4) Compile the neural network
# 5) Fitting the model to the training set
# 6) Making predictions and evaluating the model
# 7) Improving our model
# 8) Save and load the model

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# 1) Download or get the data
dataframe = pd.read_csv('realestate.csv')
print(dataframe.head())

X = dataframe[['bedrooms', 'bathrooms']].values
y = dataframe['price'].values

# 2) Data preprocessing
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
y = (y - mean) / std

# 3) Building the neural network
model = Sequential()
model.add(Dense(1, input_dim=2, activation='linear'))
model.compile(loss='mse', optimizer=Adam(lr=0.1), metrics=['mse'])

# 4) Compile the neural network
model.fit(X, y, epochs=500, verbose=0)

# 5) Making predictions and evaluating the model
predictions = model.predict(X).flatten()
for i in range(len(predictions)):
    print('Predicted: {:.3f}, Real: {:.3f}'.format(predictions[i], y[i]))

# 6) Improving our model
model.fit(X, y, epochs=500, verbose=0)
for i in range(len(predictions)):
    print('Predicted: {:.3f}, Real: {:.3f}'.format(predictions[i], y[i]))
    plt.scatter(y, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.show()

# 7) Save and load the model
model.save('realestate.h5')
del model
model = Sequential()
model.add(Dense(1, input_dim=2, activation='linear'))
model.compile(loss='mse', optimizer=Adam(lr=0.1), metrics=[ 'mse'])
model.load_weights('realestate.h5')
print("Loaded model from disk")

# 8) Making predictions and evaluating the model
predictions = model.predict(X).flatten()
for i in range(len(predictions)):
    print('Predicted: {:.3f}, Real: {:.3f}'.format(predictions[i], y[i]))
    plt.scatter(y, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.show()
    plt.close()
    plt.clf()

plt.plot(predictions, y)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.show()