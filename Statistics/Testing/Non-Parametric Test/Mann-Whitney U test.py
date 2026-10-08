import pandas as pd
from scipy.stats import mannwhitneyu
df = pd.DataFrame({
    "Group_A": [72, 65, 80, 55, 90, 68, 74, 60, 83, 77],
    "Group_B": [61, 70, 58, 75, 69, 64, 82, 67, 73, 59]
})

stat,p_val=mannwhitneyu(df["Group_A"],df["Group_B"],alternative='two-sided')

print(stat)
print(p_val)

if p_val<0.05:
    print("Reject H0")
else:
    print("Fail to Reject H0")