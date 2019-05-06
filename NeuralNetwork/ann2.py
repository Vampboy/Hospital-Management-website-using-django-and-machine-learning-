# Artificial Neural Network

# Installing Tensorflow and Keras
 
# 1. On Mac: open "Terminal"
#    On Windows: open "Anaconda Prompt"  

# 2. Type:
# conda install tensorflow
# conda install -c conda-forge keras
# conda update --all


# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.externals import joblib

# Importing the dataset
dataset = pd.read_csv('ee_20090101_20090630.csv')
#print(dataset.head())
X = dataset.iloc[:, [4,7,8,17,18,19,20]].values
#print(X)
#print(np.shape(X))
y = dataset.iloc[:, 26].values


from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy='mean' , axis=0 )
imputer = imputer.fit(X[:, 2:7])
X[:, 2:7] = imputer.transform(X[:, 2:7])


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_filename = "labelencoder.save"
joblib.dump(labelencoder_X_1, labelencoder_filename)
#print(X[:5,:])
#labelencoder_X_2 = LabelEncoder()
#X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
OneHotencoder_filename = "OneHotencoder.save"
joblib.dump(onehotencoder, OneHotencoder_filename)
#print(X[:5,:])
X = X[:, 1:]
#print(X)
#exit()
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
Stand_scalar = "Stand_scalar.save"
joblib.dump(sc, Stand_scalar)
X_test = sc.transform(X_test)


# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'relu', input_dim = 19))

# Adding the second hidden layer
classifier.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
#classifier.add(Dense(units = 4, kernel_initializer = 'uniform', activation = 'softmax'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
#classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
print(X_train.shape,y_train.shape)
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)

y_pred = (y_pred > 0.5)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#this is how im saving m models and other important parameters
classifier.save("Hospital_Model.h5")