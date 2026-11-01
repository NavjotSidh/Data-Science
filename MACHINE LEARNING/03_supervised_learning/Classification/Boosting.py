import pandas as pd
import seaborn as sns
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
df=sns.load_dataset('iris')
X=df.drop('species',axis=1)
Y=df['species']
lb=LabelEncoder()
Y=lb.fit_transform(Y)

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
model_AB=AdaBoostClassifier(n_estimators=100,random_state=42)
model_AB.fit(x_train,y_train)

model_GB=GradientBoostingClassifier(n_estimators=100,learning_rate=0.1,random_state=42)
model_GB.fit(x_train,y_train)

model_XGB=XGBClassifier(n_estimators=100,learning_rate=1,random_state=42)
model_XGB.fit(x_train,y_train)

y_pred_AB=model_AB.predict(x_test)
y_pred_GB=model_GB.predict(x_test)
y_pred_XGB=model_XGB.predict(x_test)

print(f"Ada Boost {accuracy_score(y_test,y_pred_AB)*100}%")
print(f"Graadient Boost {accuracy_score(y_test,y_pred_GB)*100}%")
print(f"XGBoost {accuracy_score(y_test,y_pred_XGB)*100}%")