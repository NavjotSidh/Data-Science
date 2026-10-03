import numpy as np
import seaborn as sns
import statistics
df=sns.load_dataset('tips')
print(df)

Mean=np.mean(df['tip'])
print("Mean = ",Mean)

Median=np.median(df['tip'])
print("Median = ",Median)

Mode=statistics.mode(df['tip'])
print("Mode = ",Mode)

P=np.percentile(df['total_bill'],[20,95])
print(P)