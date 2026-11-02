import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
plt.subplot(1,2,1)
sns.histplot(df['total_bill'],bins=10,kde=True)

plt.subplot(1,2,2)
sns.histplot(df['tip'],bins=10,kde=True)

plt.show()