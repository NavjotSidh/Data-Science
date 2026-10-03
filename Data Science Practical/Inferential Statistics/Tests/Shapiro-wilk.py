import pandas as pd
from scipy.stats import shapiro
from scipy.stats import wilcoxon, ttest_rel
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Ipl 2026\matches.csv")
diff=(df["first_ings_score"]-df["second_ings_score"]).dropna()

stat,p=shapiro(diff)


diff = (df['first_ings_score'] - df['second_ings_score']).dropna()
first = df['first_ings_score']
second = df['second_ings_score']

t_stat, t_p = ttest_rel(first, second, nan_policy='omit')
w_stat, w_p = wilcoxon(diff)

print("Paired t-test   :", t_stat, t_p)
print("Wilcoxon signed :", w_stat, w_p)