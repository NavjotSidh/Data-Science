import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Machine learning\insurance.csv")
df['sex']=df['sex'].map({'male':0,"female":1})
df['smoker']=df['smoker'].map({'no':0,"yes":1})
df.rename(columns={'sex':'is_female','smoker':'is_smoker'},inplace=True)
df=pd.get_dummies(df,columns=['region'],drop_first=True)
df=df.astype(int)
df['bmi_category']=pd.cut(
    df['bmi'],bins=[0,18.5,24.9,29.9,float('inf')],
    labels=['Underweight','Normal','Overweight','Obese'])
df=pd.get_dummies(df,columns=['bmi_category'])
df=df.astype(int)

# Feature Extraction
selected_features=['age', 'is_female', 'bmi', 'children', 'is_smoker',
'region_northwest', 'region_southeast', 'region_southwest',
       'bmi_category_Underweight', 'bmi_category_Normal',
       'bmi_category_Overweight', 'bmi_category_Obese']
correlation={feature:pearsonr(df[feature],df['charges'])[0] for feature in selected_features}
correlation_df=pd.DataFrame(list(correlation.items()),columns=['Feature','Pearson correlation'])
print(correlation_df)
correlation_df.sort_values(by='Pearson correlation',ascending=False)
print(correlation_df)