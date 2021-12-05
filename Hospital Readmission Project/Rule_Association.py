import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

class RuleLearningUtility(object):
    @staticmethod
    def getPatterns(dataFrame):
        le = dataFrame.copy()
        #Apriori needs categorical values encoded
        categorical_cols = ['race', 'gender', 'age', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id',
                         'diag_1', 'diag_2', 'diag_3', 'readmitted']

        # Encode dataFrame
        DataFrameEncoded = pd.get_dummies(le[categorical_cols], columns = categorical_cols)

        ("\nData with encoding:")
        print(DataFrameEncoded) 
        DataFrameEncoded.to_csv(r"C:\Users\14235\Desktop\File Name.csv")
        #collecting the inferred rules in a dataframe
        freq_items = apriori(DataFrameEncoded, min_support=0.3, use_colnames=True, max_len=4, verbose=1, low_memory=False)
        print(freq_items)
        print("\n")
        rules = association_rules(freq_items, metric="confidence", min_threshold=0.3)
        rules.to_csv(r"C:\Users\14235\Desktop\File Name2.csv")
        print("\n All Rules:")
        print(rules.head())
        
        return rules
    