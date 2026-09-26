import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Anime\anime.csv")

# Make a new column for episode count
def extract_feature(text):
    data=""
    check=False
    for i in  text:
        if i==')':
            break
        if i=='(':
            check=True
        if check == True:
            data+=i
    return data[1:]
df['Episodes']=df['Title'].apply(extract_feature)
df['Episodes']=df['Episodes'].str.replace(" eps","")
df['Episodes']=df['Episodes'].astype(int)
# print(df.head())
# a=df.loc[1]['Episodes']
# print(type(a))


# Make a new column for time stamp
def extract_Time_stamp(text):
    data=""
    check=False
    count=0
    for i in text:
        if count>19:
            break
        if i==')':
            check=True
        if check == True:
            data+=i
            count+=1
    return data[1:]
# df['Time_stamp']=df['Title'].apply(extract_Time_stamp)
# print(df.loc[1]['Title'])
# print(df.head())


# Series with highest rating
# print(df[df['Score']==df['Score'].max()])


#which series has heightest episodes
# print(df[df["Episodes"]==max(df['Episodes'])])

# Anime with top 5 episode counts
a=sorted(df["Episodes"].unique(),reverse=True)
# print(df[df['Episodes'].isin(a[:5])])
# print(df[df['Episodes'].isin(df["Episodes"].nlargest(5))])