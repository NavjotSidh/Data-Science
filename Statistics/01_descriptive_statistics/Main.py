import pandas as pd
from pandas.core.groupby import groupby

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Statistics\employees.csv")
print(df.head())
# "What is the average salary of our employees?"
# print("Mean is",df['Salary'].mean())
# print("Median is",df['Salary'].median())
# print("Mode is",df['Salary'].mode())

# Salary spread
# print("Minimum salary",df['Salary'].min())
# print("Maximum salary",df['Salary'].max())
# print("Range of salary",df['Salary'].max()-df['Salary'].min())
# print("Std of salary",df['Salary'].std())
# print("variance of salary",df['Salary'].var())


# Percentiles
# 25th percentile
# print("25%",df["Salary"].quantile(0.25))

# 50th percentile
# print("50%",df["Salary"].quantile(0.50))

# 75th percentile
# print("75%",df["Salary"].quantile(0.75))

# 90th percentile
# print("90%",df["Salary"].quantile(0.90))

# "Which department has the greatest salary variability?"
cat=df.groupby('Department')["Salary"].std()
# print(cat)

#Variance vs Standard Deviation
print("Std of salary",df['Salary'].std())
print("variance of salary",df['Salary'].var())