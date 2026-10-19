import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.pylabtools import figsize

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Machine learning\insurance.csv")
# print(df.head())
# print(df['sex'].value_counts())
df['sex']=df['sex'].map({'male':0,"female":1})
df['smoker']=df['smoker'].map({'no':0,"yes":1})
df.rename(columns={'sex':'is_female','smoker':'is_smoker'},inplace=True)
df=pd.get_dummies(df,columns=['region'],drop_first=True)
df=df.astype(int)
print(df.head())