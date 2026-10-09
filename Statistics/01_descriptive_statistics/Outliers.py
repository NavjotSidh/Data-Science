import pandas as pd
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Statistics\employees.csv")
# print(df.head())
Q1=df['Salary'].quantile(0.25)
Q3=df['Salary'].quantile(0.75)
iqr=Q3-Q1

lower_fence= Q1 - 1.5 * iqr
upper_fence = Q3 + 1.5 * iqr
# print(lower_fence,upper_fence)

outliers=df[(df["Salary"]<lower_fence) | (df["Salary"]>upper_fence)]
# print(outliers)

