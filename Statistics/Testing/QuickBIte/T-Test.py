import pandas as pd
from scipy.stats import shapiro,ttest_1samp,t

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Statistics\quickbite_customers.csv")
data=df["delivery_time_after"].dropna()
mean=data.mean()
sem=data.sem()
ci=t.interval(confidence=0.95,df=len(data)-1,loc=mean,scale=sem)
print("Mean ",mean)
print("95% Confidence Interval ",round(ci[0],2)," to ",round(ci[1],2))

# print(df.columns)
stat,p=shapiro(data)
print("Shapiro Statistics ",stat," Shapiro P-Value ",p)

s,p_val=ttest_1samp(data,28)
print("T-test Statistics ",s,"T-test P-Value ",p_val)
