import pandas as pd

df1 = pd.DataFrame({
    'Name': ['John', 'Arya'],
    'Age': [22, 18]
})

df2 = pd.DataFrame({
    'Name': ['Sansa', 'Ned'],
    'Age': [21, 40]
})
res=pd.concat([df1,df2],axis=0)
print(res)