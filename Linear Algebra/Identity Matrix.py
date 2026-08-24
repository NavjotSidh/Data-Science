import numpy as np
A = np.array([
    [1, 2],
    [3, 4]
])
i=np.eye(2)
print(A@i)
print(i@A)