import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from sklearn.externals import joblib

class Hospital_pred():

    def __init__(self):

        self.classifier=load_model("NeuralNetwork/Hospital_Model.h5")

    def filter_data(self,X):
        #list=['age','mode','triage','blood','heart','breathing','temp']
        #labelencoder = joblib.load("NeuralNetwork/labelencoder.save") 
        #X[:,1] = labelencoder.transform(X[:,1])
        #print(X)
        onehotencoder = joblib.load("NeuralNetwork/OneHotencoder.save") 
        X = onehotencoder.transform(X).toarray()
        X = X[:,1:]
        
        sc = joblib.load("NeuralNetwork/Stand_scalar.save") 
        X = sc.transform(X)
        #print(X)

        return X


    def getpredictor(self,in_data):
        in_data=self.filter_data(in_data)
        prediction = self.classifier.predict(in_data)
        return prediction



#temp=Hospital_pred()
#print(float(temp.getpredictor([19,2,0,2,149,87,18,36.7]))*100)