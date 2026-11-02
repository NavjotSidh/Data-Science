import seaborn as sns
import matplotlib.pyplot as plt
flights=sns.load_dataset('flights')
print(flights.columns)

pvtflight=flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvtflight)
plt.show()