import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
df=sns.load_dataset('iris')
X=df.drop('species',axis=1)
Y=df['species']

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
model_RF=RandomForestClassifier(n_estimators=100,max_depth=None,random_state=42)
model_RF.fit(x_train,y_train)
y_pred=model_RF.predict(x_test)

accuracy=accuracy_score(y_test,y_pred)
print(f"{accuracy*100}%")