import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from packaging import markers
from scipy.constants import pt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X,y_true=make_blobs(n_samples=500,centers=3,cluster_std=0.60,random_state=42)
df=pd.DataFrame(X,columns=["F1","F2"])
scaler=StandardScaler()
X_scaled=scaler.fit_transform(df)

inertia=[]
K_range=range(1,11)
for k in K_range:
    k_means=KMeans(n_clusters=k,random_state=42)
    k_means.fit(X_scaled)
    inertia.append(k_means.inertia_)

# plt.plot(K_range,inertia,marker=0)
# plt.show()

k_means_final=KMeans(n_clusters=3,random_state=42)
cluster_label=k_means_final.fit_predict(X_scaled)
df['Cluster']=cluster_label

sns.scatterplot(x=df['F1'],y=df['F2'],hue=df['Cluster'],palette='viridis')
plt.show()