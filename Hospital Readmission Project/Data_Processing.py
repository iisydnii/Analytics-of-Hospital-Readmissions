import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from pandas.core.frame import DataFrame

class ProcessingUtility(object):

    # Data Processing - Part 1
    # What are the attributes (columns) that have missing data more than 50%?
    @staticmethod
    def setMissingValuesToNaN(dataFrame):
        dataFrame = dataFrame.replace('?', np.NaN)
        dataFrame = dataFrame.replace('Not Available', np.NaN)
        dataFrame = dataFrame.replace('', np.NaN)
        dataFrame = dataFrame.replace('None', np.NaN)
        return dataFrame

    @staticmethod
    def getNaNStats (dataFrame):
        print("\nTotal NaN count for each column:")
        isNaNperCol = dataFrame.isna().sum()
        print(isNaNperCol.to_string())

        print("\nPercentage of NaN values:")
        
        i = 0
        for col in isNaNperCol:
            i += 1
            percentageNaN = (col/10000)*100
            print(i, ":  ", percentageNaN, "%")

        return [isNaNperCol, percentageNaN]

    @staticmethod
    def dropDirtyCols(dataFrame, colsTODrop):
        dataFrame = dataFrame.drop(colsTODrop, axis=1)
        return dataFrame

    @staticmethod
    def imputeMissingValues(dataFrame, numNeighbors, colsToImpute):
        for col in colsToImpute:
            dataFrame[col] = dataFrame [col].fillna(dataFrame[col].mode()[0])
        
        return dataFrame

    @staticmethod
    def setNaNValuesOfCol(dataFrame, col, value):
        dataFrame[col] = dataFrame[col].fillna(value)
        
        return dataFrame

    @staticmethod
    def trim(dataFrame, factor):
        dataFrame.to_csv('dataset.csv')
        numeric_cols = ['time_in_hospital', 'num_lab_procedures', 'num_procedures', 'num_medications', 'number_outpatient', 'number_emergency',
                    'number_inpatient', 'number_diagnoses' ]
        for col in numeric_cols:
            upper_lim = dataFrame[col].mean () + dataFrame[col].std () * factor
            lower_lim = dataFrame[col].mean () - dataFrame[col].std () * factor
            dataFrame = dataFrame[(dataFrame[col] < upper_lim) & (dataFrame[col] > lower_lim)]
        dataFrame.to_csv('dataset2.csv')
        return dataFrame
    
    @staticmethod
    def encodeForModeling(dataFrame):
        le = LabelEncoder()
        categorical_cols = ['race', 'gender', 'age', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id',
                         'diag_1', 'diag_2', 'diag_3','diabetesMed' ,'readmitted']
        
        dataFrame = dataFrame[categorical_cols]

        dataFrame[categorical_cols] = dataFrame[categorical_cols].fillna('NaN')
        dataFrame['readmitted'] = dataFrame['readmitted'].replace('Yes', 1)
        dataFrame['readmitted'] = dataFrame['readmitted'].replace('No', 0)
        dataFrame['diabetesMed'] = dataFrame['diabetesMed'].replace('Yes', 1)
        dataFrame['diabetesMed'] = dataFrame['diabetesMed'].replace('No', 0)
        dataFrame['gender'] = dataFrame['gender'].replace('Male', 1)
        dataFrame['gender'] = dataFrame['gender'].replace('Female', 0)

        
        st_data = dataFrame['race']
        st_data = pd.get_dummies(st_data)
        
        for col in st_data:
             dataFrame[col] = st_data[col]

        dataFrame = dataFrame.drop(columns=['race'])
        st_data = dataFrame['age']
        st_data = pd.get_dummies(st_data)
        
        for col in st_data:
             dataFrame[col] = st_data[col]

        dataFrame = dataFrame.drop(columns=['age'])
        st_data = dataFrame['admission_type_id']
        st_data = pd.get_dummies(st_data)
        
        for col in st_data:
             dataFrame[col] = st_data[col]

        dataFrame = dataFrame.drop(columns=['admission_type_id'])
        st_data = dataFrame['discharge_disposition_id']
        st_data = pd.get_dummies(st_data)
        
        for col in st_data:
             dataFrame[col] = st_data[col]
        
        dataFrame = dataFrame.drop(columns=['discharge_disposition_id'])
        st_data = dataFrame['admission_source_id']
        st_data = pd.get_dummies(st_data)
        
        for col in st_data:
             dataFrame[col] = st_data[col]
        dataFrame = dataFrame.drop(columns=['admission_source_id'])
        st_data = dataFrame['diag_1']
        st_data = pd.get_dummies(st_data)
        
        for col in st_data:
             dataFrame[col] = st_data[col]
        dataFrame = dataFrame.drop(columns=['diag_1'])
        st_data = dataFrame['diag_2']
        st_data = pd.get_dummies(st_data)
        
        for col in st_data:
             dataFrame[col] = st_data[col]
        dataFrame = dataFrame.drop(columns=['diag_2'])
        st_data = dataFrame['diag_3']
        st_data = pd.get_dummies(st_data)
        
        for col in st_data:
             dataFrame[col] = st_data[col]
        dataFrame = dataFrame.drop(columns=['diag_3'])
        
        return dataFrame