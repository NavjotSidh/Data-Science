import pandas as pd
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Statistics\employees.csv")
mean_salary= df.groupby('Department')["Salary"].mean()
std_salary= df.groupby('Department')["Salary"].std()

cv = (std_salary / mean_salary) * 100

result = pd.DataFrame({
    "Mean Salary": mean_salary,
    "Std Salary": std_salary,
    "CV (%)": cv
})
print(result)