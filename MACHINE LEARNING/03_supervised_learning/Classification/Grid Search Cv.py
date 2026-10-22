import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df=sns.load_dataset('iris')
X=df.drop('species',axis=1)
y=df['species']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
score=model.score(x_test,y_test)
print(score)