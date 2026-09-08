import numpy as np
a = np.array([
    [2, 1],
    [1, 1]
])
a_inv=np.linalg.inv(a)
print(a)
print(a_inv)
print(a@a_inv)