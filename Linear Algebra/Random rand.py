import numpy as np
A = np.random.randint(1, 10, (1000, 4))
B= np.random.randint(1, 10, (4, 4958))

print(np.shape(A@B))