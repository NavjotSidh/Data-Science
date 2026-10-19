import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.pylabtools import figsize

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Machine learning\insurance.csv")

df['bmi_category']=pd.cut(
    df['bmi'],bins=[0,18.5,24.9,29.9,float('inf')],
    labels=['Underweight','Normal','Overweight','Obese']
)
df=pd.get_dummies(df,columns=['bmi_category'])
print(df.head())