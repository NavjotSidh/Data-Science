import numpy as np
a=np.array([
    [2, 0],
    [0, 3]
])

eigenvalue,eigenvector=np.linalg.eig(a)
print(eigenvalue)
print(eigenvector)