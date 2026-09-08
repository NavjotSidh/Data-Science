import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")

sns.boxplot(x=df['total_bill'])
plt.show()