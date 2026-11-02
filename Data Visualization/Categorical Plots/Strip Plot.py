import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
plt.subplot(1,2,1)
sns.stripplot(x='day',y='total_bill',data=df)
plt.subplot(1,2,2)
sns.swarmplot(x='day',y='total_bill',data=df)

plt.show()