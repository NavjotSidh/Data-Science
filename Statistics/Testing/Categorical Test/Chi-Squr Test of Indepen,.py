import pandas as pd
from scipy.stats import chi2_contingency
df = pd.DataFrame({
    "Gender": ["Male", "Male", "Male", "Male", "Male",
               "Female", "Female", "Female", "Female", "Female"],

    "Preference": ["A", "A", "B", "B", "B",
                   "A", "A", "A", "B", "B"]
})
df["Preference"] = df["Preference"].map({
    "A": "Offline",
    "B": "Online"
})
table = pd.crosstab(df["Gender"], df["Preference"])

print(table)
chi2,p,dof,expected=chi2_contingency(table)
print("Chi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)

print("Expected frequencies:")
print(expected)

if p < 0.05:
    print("Reject H0")
else:
    print("Fail to reject H0")
