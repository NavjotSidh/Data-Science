import pandas as pd

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Anime\Countries.csv")
# print(df.columns)
# Q1 Country with highest population
# print(df[df['population']==df['population'].max()])

# Q2 Captital of country with highest polulation
# print(df[df['democracy_score'].isin(df['democracy_score'].nlargest(5))])

# Q3 Total no of regions
# print(df['region'].value_counts().count())

# Q4 Country in eartern europe
# print(df['region'].value_counts()['Eastern Europe'])

# Q5 Leader of 2nd highest populated country
# print(df[df['population']==df['population'].nlargest(2).iloc[1]]['political_leader'])

# Q6 Country with Republic in thier name
count=0
def counting(text):
    global count
    if 'republic' in text.lower():
        count+=1
    return text
df['country_long']=df['country_long'].apply(counting)
print(count)