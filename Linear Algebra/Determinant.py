import numpy as np
# a=np.random.randint(1,10,(2,2))
a = np.array([
    [1, 2],
    [2, 4]
])
d=np.linalg.det(a)
print(d)

if np.isclose(d,0)==0:
    print("Singular")
else:
    print("not Singular")