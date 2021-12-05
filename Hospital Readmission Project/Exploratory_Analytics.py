import numpy as np
import matplotlib.pyplot as plt

class AnalyticsUtility(object):
    #Bar charts
    @staticmethod
    def plotReadmitts (dataset):
        plt.title('Patients Readmitted vs Non-Readmitted Patients')
        plt.xlabel('Categories')
        plt.ylabel('Values')
        
        dataset['readmitted'].value_counts().plot(kind='bar')
        print('\n readmitted - No \n')
        print(sum(AnalyticsUtility.condition_No(x) for x in dataset['readmitted']))

        print('\n readmitted - Yes \n')
        print(sum(AnalyticsUtility.condition_Yes(x) for x in dataset['readmitted']))
        plt.show()
        return dataset

    @staticmethod
    def plotDiabetesMeds (dataset):
        plt.title('Patients on Diabetic Medication vs Patients Who Are Not')
        plt.xlabel('Categories')
        plt.ylabel('Values')
        
        dataset['diabetesMed'].value_counts().plot(kind='bar')
        print('\n diabetesMed - No \n')
        print(sum(AnalyticsUtility.condition_No(x) for x in dataset['diabetesMed']))

        print('\n diabetesMed - Yes \n')
        print(sum(AnalyticsUtility.condition_Yes(x) for x in dataset['diabetesMed']))
        plt.show()
        return dataset

    @staticmethod
    def plotPassedPatients (dataset):
        plt.title('Patients Who Have Passed vs Patients Who Have Not')
        plt.xlabel('Categories')
        plt.ylabel('Values')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged to home', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred to home with home health service', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred to a long term care hospital.', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred to SNF', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred to another  type of inpatient care institution', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred to another short term hospital', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged to home', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Hospice / medical facility', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred to another rehab fac including rehab units of a hospital.', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred/referred to a psychiatric hospital of a psychiatric distinct part unit of a hospital', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred to ICF', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Left AMA', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred to home under care of Home IV provider', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Hospice / home', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace('Discharged/transferred within this institution to Medicare approved swing bed', 'Not Expired')
        dataset['discharge_disposition_id'] = dataset['discharge_disposition_id'].replace( np.NaN, 'NaN')
        
        dataset['discharge_disposition_id'].value_counts().plot(kind='bar')
        print('\n discharge_disposition_id - Expired \n')
        print(sum(AnalyticsUtility.condition_Expired(x) for x in dataset['discharge_disposition_id']))

        print('\n discharge_disposition_id - Not Expired \n')
        print(sum(AnalyticsUtility.condition_NotExpired(x) for x in dataset['discharge_disposition_id']))
        plt.subplots_adjust(bottom=0.25)
        plt.show()
        dataset['discharge_disposition_id'].to_csv('discharge_disposition_id.csv')
        return dataset
    
    @staticmethod
    def plotDemographics (dataset):
        data = dataset[['age', 'gender', 'race']]
        
        gender_column = data['gender']
        age_column = data['age']
        data.groupby(["race", age_column, gender_column]).size().unstack(level=2).plot(kind='bar')
        
        plt.subplots_adjust(bottom=0.320, right=1)
        plt.show()
        return dataset

    @staticmethod
    def condition_No(x):
        return x == 'No'
    
    @staticmethod
    def condition_Yes(x):
        return x == 'Yes'
    
    @staticmethod
    def condition_Expired(x):
        return x == 'Expired'
    
    @staticmethod
    def condition_NotExpired(x):
        return x == 'Not Expired'