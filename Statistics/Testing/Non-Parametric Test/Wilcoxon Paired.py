import pandas as pd
from scipy.stats import wilcoxon
df = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20],

    "Before": [72, 65, 80, 55, 90, 68, 74, 60, 83, 77,
               69, 58, 85, 71, 66, 79, 62, 88, 73, 57],

    "After": [75, 68, 82, 60, 88, 72, 76, 65, 85, 79,
              70, 63, 87, 73, 69, 81, 67, 90, 74, 61]
})

stat,p_val=wilcoxon(df["Before"],df["After"])

print(stat)
print(p_val)

if p_val<0.05:
    print("Reject H0")
else:
    print("Fail to Reject H0")