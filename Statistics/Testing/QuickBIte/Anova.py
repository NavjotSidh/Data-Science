import pandas as pd
from scipy.stats import shapiro,f_oneway
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Statistics\quickbite_customers.csv")

delhi=df.loc[df["city"]=="Delhi","delivery_time_before"].dropna()
bengaluru=df.loc[df["city"]=="Bengaluru","delivery_time_before"].dropna()
chennai=df.loc[df["city"]=="Chennai","delivery_time_before"].dropna()
mumbai=df.loc[df["city"]=="Mumbai","delivery_time_before"].dropna()

delhi_mean=delhi.mean()
bengaluru_mean=bengaluru.mean()
chennai_mean=chennai.mean()
mumbai_mean=mumbai.mean()

print("Delhi :",delhi_mean,"Bengaluru :",bengaluru_mean,"Chennai :",chennai_mean,"Mumbai :",mumbai_mean)
s1,p1=shapiro(delhi)
s2,p2=shapiro(bengaluru)
s3,p3=shapiro(chennai)
s4,p4=shapiro(mumbai)

print("Shapiro :",p1,p2,p3,p4)
stat,p_val=f_oneway(delhi,bengaluru,chennai,mumbai)
print("Anova P value :",p_val)