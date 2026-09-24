import pandas as pd
data={
    'Name' : ['John','Arya','Sansa','Ned'],
    'Age' : [22,18,21,40],
    'City' : ['NYC','Paris','Berlin','London'],
    'Salary' : [65000,70000,62000,85000]
}
df=pd.DataFrame(data)
df['Designation']=['Prince','Hitman','Queen','King']
print(df[(df['Salary']>=65000) & ( df["City"]=='Paris')])