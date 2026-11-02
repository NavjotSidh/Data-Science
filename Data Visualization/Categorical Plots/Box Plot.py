import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.boxplot(x='tip',y='day',data=df,palette='rainbow')
plt.show()