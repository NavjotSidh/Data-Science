import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = [48, 49, 50, 51, 50,49, 51, 50, 48, 52,49, 50, 51, 50, 49,52, 50, 48, 100]


outliers=[]
def find_outliers(data):
    threshold=2
    m=np.mean(data)
    s=np.std(data)
    for i in data:
        z_score=(i-m)/s
        if np.abs(z_score)>threshold:
            outliers.append(i)
            data.remove(i)
    return outliers
find_outliers(data)
print(outliers)

sns.boxplot(data)
plt.show()
