import numpy as np
A=np.array([[3,1,2],[4,3,5]])
print(A)
print(A.shape)
print(A.ndim)
print(len(A))

#Vector indexing
v = np.array([10, 20, 30, 40, 50])

print(v[0])
print(v[2])
print(v[-1])

#slicing
print(v[1:4])
print(v[:3])
print(v[2:])
