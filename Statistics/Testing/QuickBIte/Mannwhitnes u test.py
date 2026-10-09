import pandas as pd
from scipy.stats import levene,mannwhitneyu
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Statistics\quickbite_customers.csv")

lunch=df.loc[df["meal_slot"]=="Lunch","delivery_time_before"].dropna()
dinner=df.loc[df["meal_slot"]=="Dinner","delivery_time_before"].dropna()

stat1,p1=levene(lunch,dinner)
# print(p1)
median_lunch=lunch.median()
median_dinner=dinner.median()
print("Median_lunch :",median_lunch,"   Median_dinner :",median_dinner)

stat,p_val=mannwhitneyu(lunch,dinner,alternative='two-sided')
print("P value :",p_val)