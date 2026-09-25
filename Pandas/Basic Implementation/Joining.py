import pandas as pd
df1 = pd.DataFrame({
    'Name': ['John', 'Arya', 'Sansa'],
    'Age': [22, 18, 21]
})

df2 = pd.DataFrame({
    'City': ['NYC', 'Paris', 'Berlin'],
    'Salary': [65000, 70000, 62000]
})
result=df1.join(df2)
print(result)