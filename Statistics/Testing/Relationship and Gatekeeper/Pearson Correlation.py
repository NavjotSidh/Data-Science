import pandas as pd
from scipy.stats import pearsonr
df = pd.DataFrame({
    "Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Marks": [40, 45, 52, 58, 65, 70, 76, 82, 88, 95]
})

r,p_val=pearsonr(df["Hours"],df["Marks"])
print("Correlation ",r)
print("P-Value",p_val)
if p_val < 0.05:
    print("Reject H0")
else:
    print("Fail to reject H0")
