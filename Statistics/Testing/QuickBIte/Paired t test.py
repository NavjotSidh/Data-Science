import pandas as pd
from scipy.stats import shapiro,ttest_rel,t
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Statistics\quickbite_customers.csv")
# print(df.columns)
data = df[["delivery_time_before", "delivery_time_after"]].dropna()

data1=data["delivery_time_before"]
data2=data["delivery_time_after"]
diff = data1 - data2
# print(diff)
mean1=data1.mean()
mean2=data2.mean()
print("Mean Difference :",abs(mean2-mean1))

stat1,p1=shapiro(diff)
print("Shapiro P value ",p1)

stat,p_val=ttest_rel(data1,data2)
print("P value :",p_val)

ci=t.interval(confidence=0.95,df=len(diff)-1,loc=diff.mean(),scale=diff.sem())
print("Confidence interval :",round(ci[0],2),"to",round(ci[1],2))