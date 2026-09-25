import pandas as pd

df = pd.DataFrame({
    'Employee': [
        'John', 'Arya', 'Sansa', 'Ned',
        'John', 'Arya', 'Sansa', 'Ned',
        'John', 'Arya', 'Sansa', 'Ned'
    ],
    'Department': [
        'IT', 'HR', 'IT', 'Sales',
        'IT', 'HR', 'IT', 'Sales',
        'IT', 'HR', 'IT', 'Sales'
    ],
    'City': [
        'Delhi', 'Mumbai', 'Delhi', 'Pune',
        'Delhi', 'Mumbai', 'Delhi', 'Pune',
        'Delhi', 'Mumbai', 'Delhi', 'Pune'
    ],
    'Sales': [
        50000, 30000, 45000, 60000,
        70000, 35000, 55000, 75000,
        65000, 40000, 60000, 80000
    ],
    'Experience': [
        2, 3, 4, 5,
        2, 3, 4, 5,
        2, 3, 4, 5
    ]
})

print(df['Sales'].agg(['mean','median','min','max','count','sum','std']))