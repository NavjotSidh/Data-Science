import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Data Cleaning
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Machine learning\titanic.csv")
df.drop(['Cabin','Pclass','Ticket','Name'],axis=1,inplace=True)
df['Age']=df['Age'].fillna(df['Age'].mean())
df.dropna(subset=['Embarked'],inplace=True)
pd.set_option('display.max_columns', None)
# print(df.info())

# Encoding
le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])
df['Embarked']=le.fit_transform(df['Embarked'])
# print(df.head())
# Model
X=df.drop('Survived',axis=1)
y=df['Survived']

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)


#Evaluation
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print("Accuracy :",accuracy_score(y_test,y_pred))
print("Confusion_matrix :")
print(confusion_matrix(y_test,y_pred))
print("Classification_report :")
print(classification_report(y_test,y_pred))