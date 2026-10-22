import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Machine learning\cleaned_titanic.csv")

X=df.drop('Survived',axis=1)
y=df['Survived']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)
model=SVC(random_state=42)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

scores=cross_val_score(model,X,y,cv=5,scoring='accuracy')
print(scores.mean())