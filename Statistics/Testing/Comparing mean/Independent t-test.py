import pandas as pd
data = {
    "Employee": ["A","B","C","D","E","F","G","H","I","J",
                 "K","L","M","N","O","P","Q","R","S","T"],

    "Department": ["IT","IT","IT","IT","IT",
                   "HR","HR","HR","HR","HR",
                   "Finance","Finance","Finance","Finance","Finance",
                   "Sales","Sales","Sales","Sales","Sales"],

    "Salary": [52000, 55000, 58000, 54000, 57000,
               42000, 45000, 44000, 46000, 43000,
               60000, 62000, 65000, 61000, 64000,
               48000, 51000, 50000, 53000, 49000],

    "Experience": [2,3,4,3,5,
                   1,2,2,3,1,
                   5,6,7,5,6,
                   2,3,3,4,2],

    "Before_Training": [62,68,71,65,70,
                        55,60,58,63,57,
                        72,75,78,70,74,
                        61,64,60,67,63],

    "After_Training": [70,75,78,73,79,
                       63,68,67,71,65,
                       80,84,86,79,82,
                       69,72,68,75,71]
}
df = pd.DataFrame(data)
print(df)
groups = df.groupby("Department")["Salary"]

Finance_salary = groups.get_group("Finance")
Sales_salary = groups.get_group("Sales")

from scipy.stats import ttest_ind
t_stat,p_value=ttest_ind(Finance_salary,Sales_salary,equal_var=False)
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value<0.05:
    print("Reject h0")
else:
    print("Fail to reject h0")