import numpy as np
s = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])
def is_vald(s):
    r=np.sum(s,axis=1)
    c=np.sum(s,axis=0)
    for i in r:
        if i!=45:
            return False
    for j in c:
        if j != 45:
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            n=s[i:i+3,j:j+3]
            if np.sum(n) != 45:
                return False
    return True

print(is_vald(s))
