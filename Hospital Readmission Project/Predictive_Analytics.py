import pandas as pd
import numpy as np
from sklearn import metrics 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split  
from sklearn.tree import DecisionTreeClassifier 
from sklearn import metrics 
from sklearn.naive_bayes import GaussianNB 

class PredictiveUtility(object):
    @staticmethod
    def predict(dataFrame):
        x = dataFrame.drop(['readmitted'], axis=1)
        y = dataFrame['readmitted']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # Create and Train Decision Tree Classifer object
        clf = DecisionTreeClassifier()
        clf = clf.fit(x_train,y_train)

        # Predict the resonse for test dataset
        y_pred = clf.predict(x_test)
        print('\nDecision Tree: \n')
        results = metrics.confusion_matrix(y_test, y_pred)
        print("Confusion Matrix:\n", results)

        # Evaluating model accuracy 
        print("Accuracy:\n", metrics.classification_report(y_test, y_pred))

        model = GaussianNB()
        print('\nGaussian Naive Bayes: \n')
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        results = metrics.confusion_matrix(y_test, y_pred)
        print("Confusion Matrix:\n", results)
        print("Accuracy:\n", metrics.classification_report(y_test, y_pred))
        
        return dataFrame
    