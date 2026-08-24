#Scalar
import numpy as np
v = np.array([2, 3, 4])
# print(v*3)

#vector
a=np.array([5,4,6])
print(v*a)
#dot product
print(np.dot(v,a))

# Vector magnitude
mag=np.linalg.norm(v)
print(mag)