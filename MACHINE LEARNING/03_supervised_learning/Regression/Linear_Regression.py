import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Machine learning\linear_regression_advertising_sales_100_rows.csv")
X=df["Advertising_Spend"].values.reshape(-1,1)
Y=df["Sales"].values

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

lr=LinearRegression()
lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)
r2=r2_score(y_test,y_pred)

plt.scatter(x_test,y_test,color="black",label="Actual")
plt.plot(x_test,y_pred,color='red',label="Predicted")
plt.legend(loc='best')
# plt.show()

print(lr.predict([[6540]]))