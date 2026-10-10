import pandas as pd
from scipy.stats import shapiro,f_oneway,levene,mannwhitneyu

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Statistics\quickbite_customers.csv")
new=df.loc[df["customer_type"]=="New","monthly_spend_before"].dropna()
returning=df.loc[df["customer_type"]=="Returning","monthly_spend_before"].dropna()

median_return=returning.median()
median_new=new.median()
print("median of Returning :",median_return,"  median of New :",median_new)
# diff=returning-new
# print(diff)
s1,p1=shapiro(returning)
s2,p2=shapiro(new)
# s3,p3=shapiro(diff)
s4,p4=levene(returning,new)
print(p1,p2,p4)

stat,p_val=mannwhitneyu(returning,new,alternative='two-sided')
print("Mannwhitney P value :",p_val)