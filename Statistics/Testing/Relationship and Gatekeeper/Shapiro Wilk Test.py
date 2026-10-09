import pandas as pd
from scipy.stats import shapiro
df = pd.DataFrame({
    "Marks": [72, 68, 75, 80, 65, 71, 74, 69, 77, 73,
              70, 76, 81, 67, 72]
})

stat,p=shapiro(df["Marks"])
print("Statistic:", stat)
print("p-value:", p)

if p < 0.05:
    print("Reject H0: Data is not normally distributed")
else:
    print("Fail to reject H0: Data is normally distributed")