import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Ipl 2026\matches.csv")
# print(df["first_ings_score"])
# df.drop(38,inplace=True) #thats outlier
df["zscore"]=zscore(df["first_ings_score"], nan_policy="omit")

scaler=MinMaxScaler()
df["normalized_score"]=scaler.fit_transform(df[["first_ings_score"]])
print(df[["first_ings_score","zscore","normalized_score"]].describe())

