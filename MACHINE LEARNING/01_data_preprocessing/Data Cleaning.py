import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.pylabtools import figsize

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Machine learning\insurance.csv")
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isna().sum())
numeric_column=['age','bmi','children','charges']
# plt.figure(figsize=(12, 8))

# for i, col in enumerate(numeric_column):
#     plt.subplot(2, 2, i + 1)
#     sns.histplot(df[col], kde=True, bins=20)
#     plt.title(col)

# sns.countplot(x=df['children'])
# sns.countplot(x=df['smoker'])

sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.show()
