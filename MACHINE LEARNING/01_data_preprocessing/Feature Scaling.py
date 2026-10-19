import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
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

# Feature Scaling

cols=['age','bmi','children']
scaler=StandardScaler()
df[cols]=scaler.fit_transform(df[cols])
pd.set_option('display.max_columns', None)
print(df.head())
