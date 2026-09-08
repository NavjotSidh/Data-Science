import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = [49, 50, 51, 50, 49,51, 50, 52, 48, 50,51, 49, 50, 51, 49,50, 48, 52, 200, -100]

data.sort()
q1,q3=np.percentile(data,[25,75])
iqr=q3-q1
lf=q1-(1.5*iqr)
uf=q3+(1.5*iqr)
outliers=[x for x in data if x<lf or x>uf]
clean_data=[x for x in data if lf<=x<=uf]
print(clean_data)
print(outliers)
sns.boxplot(clean_data)
plt.show()
