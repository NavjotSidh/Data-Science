import seaborn as sns
import matplotlib.pyplot as plt
flights=sns.load_dataset('flights')
tips=sns.load_dataset('tips')

tipscorr=tips[['total_bill','tip','size']]
print(tipscorr.corr())
sns.heatmap(tipscorr.corr(),annot=True)
plt.show()