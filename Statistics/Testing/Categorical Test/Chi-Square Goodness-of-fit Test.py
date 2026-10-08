import pandas as pd
from scipy.stats import chisquare
df = pd.DataFrame({
    "Face": [1, 2, 3, 4, 5, 6],
    "Observed": [8, 12, 10, 9, 11, 10],
    "Expected": [10, 10, 10, 10, 10, 10]
})

stat,p_val=chisquare(df['Observed'],f_exp=df['Expected'])
print(stat)
print(p_val)

if p_val<0.05:
    print("Reject H0")
else:
    print("Fail to Reject H0")
