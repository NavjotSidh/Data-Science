import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=sns.load_dataset('tips')
sns.barplot(x=df['sex'],y=df['total_bill'],estimator=np.sum)
plt.show()