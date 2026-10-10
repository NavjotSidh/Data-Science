import numpy as np

arr=np.random.randint(0,100,size=(3,4))
print(arr)
print("Max :",arr.max())
print("Min :",arr.min())
print("Sum :",arr.sum())
print("Sum of cols :",np.sum(arr,axis=0))
print("Sum of rows :",np.sum(arr,axis=1))
print("Mean :",arr.mean())
print("Standard deviation :",arr.std())