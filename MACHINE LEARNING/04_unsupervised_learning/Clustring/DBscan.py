import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans,DBSCAN
from sklearn.preprocessing import StandardScaler

X,y_true=make_moons(n_samples=500,noise=0.05,random_state=42)
df=pd.DataFrame(X,columns=["F1","F2"])
scaler=StandardScaler()
X_scaled=scaler.fit_transform(df)

k_means_final=KMeans(n_clusters=2,random_state=42)
cluster_label=k_means_final.fit_predict(X_scaled)
df['Cluster']=cluster_label

dbscan=DBSCAN(eps=0.30,min_samples=5)
dbscan_labels=dbscan.fit_predict(X_scaled)
df['Dbscan_cluster']=dbscan_labels

sns.scatterplot(x=df['F1'],y=df['F2'],hue=df['Dbscan_cluster'],palette='tab10')

# sns.scatterplot(x=df['F1'],y=df['F2'],hue=df['Cluster'],palette='tab10')
plt.show()