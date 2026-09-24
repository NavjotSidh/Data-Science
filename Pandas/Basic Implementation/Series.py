import numpy as np
import pandas as pd

my_list=[10,20,30]
arr=np.array([10,20,30])
d={1:10,2:20,3:30}
label=['a','b','c']

print(pd.Series(my_list))
print(pd.Series(arr,index=['a','b','c']))
print(pd.Series(d))