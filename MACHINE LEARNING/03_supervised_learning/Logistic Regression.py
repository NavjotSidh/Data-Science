from sys import pycache_prefix

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,classification_report
import pandas as pd
df = pd.DataFrame({
    "attendance_pct": [30, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98],
    "dropout":        [ 1,  1,  1,  1,  1,  0,  1,  0,  0,  0,  0,  0,  0,  0]
})

X=df[['attendance_pct']]
Y=df['dropout']
# print(X,Y)
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,stratify=Y)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model=LogisticRegression(C=1.0,class_weight='balanced')
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_prob=model.predict_proba(x_test)[:,1]

print("Predictions:", y_pred)
print("Actual values:", y_test.values)
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))