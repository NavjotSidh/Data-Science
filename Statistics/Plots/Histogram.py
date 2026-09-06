import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
print(df.head())
sns.histplot(x=df['sepal_width'],kde=True)
# sns.histplot(x=df['petal_length'],kde=True)

plt.show()