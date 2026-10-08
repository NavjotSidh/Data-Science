import pandas as pd
from scipy.stats import kruskal
df = pd.DataFrame({
    "Method_A": [72, 65, 80, 55, 90, 68, 74, 60, 83, 77],
    "Method_B": [61, 70, 58, 75, 69, 64, 82, 67, 73, 59],
    "Method_C": [85, 88, 79, 92, 81, 87, 90, 84, 86, 91]
})

stat,p_val=kruskal(df["Method_A"],df["Method_B"],df["Method_C"])

print(stat)
print(p_val)

if p_val<0.05:
    print("Reject H0")
else:
    print("Fail to Reject H0")