import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Machine learning\cleaned_titanic.csv")
X=df.drop('Survived',axis=1)
y=df['Survived']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

# Evalutaion
print("Accuracy :",accuracy_score(y_test,y_pred))
print("Confusion_matrix :")
print(confusion_matrix(y_test,y_pred))
print("Classification_report :")
print(classification_report(y_test,y_pred))
