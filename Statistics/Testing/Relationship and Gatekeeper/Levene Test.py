import pandas as pd
from scipy.stats import levene
df = pd.DataFrame({
    "Class_A": [72, 75, 68, 70, 74, 71, 69, 73],
    "Class_B": [65, 80, 60, 85, 70, 75, 68, 82],
    "Class_C": [71, 73, 70, 72, 74, 69, 75, 71]
})

stat,p=levene(df["Class_A"],df["Class_B"],df["Class_C"])
print("Statistic:", stat)
print("p-value:", p)

if p < 0.05:
    print("Reject H0: Data is not normally distributed")
else:
    print("Fail to reject H0: Data is normally distributed")