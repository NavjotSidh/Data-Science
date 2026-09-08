import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
print(df.head())
sns.countplot(x=df['sepal_width'])

plt.show()