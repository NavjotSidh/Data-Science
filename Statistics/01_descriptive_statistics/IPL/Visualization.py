import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Ipl 2026\matches.csv")

# a=plt.boxplot(Max_first_inn,Q1_first_inn,Median_first_inn,Q3_first_inn,Max_first_inn
# first = df["first_ings_score"].dropna()
# second = df["second_ings_score"].dropna()

# plt.boxplot([first, second])
# plt.xticks([1, 2], ["1st Innings", "2nd Innings"])
# # plt.show()

print(df["first_ings_score"].skew())
print(df["first_ings_score"].kurt())
sns.histplot(df["first_ings_score"].dropna(),kde=True)
plt.show()
