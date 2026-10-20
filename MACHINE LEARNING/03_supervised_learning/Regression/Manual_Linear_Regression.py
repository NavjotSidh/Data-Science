import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Weeks': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Sales': [12, 25, 18, 35, 28, 45, 38, 55, 48, 65]
})
X=df["Weeks"]
Y=df["Sales"]
mean_x=np.mean(X)
mean_y=np.mean(Y)
n=len(X)
numer,denom=0,0
for i in range(n):
    numer+=(X[i]-mean_x)*(Y[i]-mean_y)
    denom+=(X[i]-mean_x)**2
m=numer/denom
c=mean_y-(m*mean_x)

max_x=max(X)+1
min_x=min(X)-1

x=np.linspace(min_x,max_x)
y=(m*x)+c
# print(x)
# print(y)

plt.plot(x,y,color="red",label="Regression",linestyle="--")
plt.scatter(X,Y,color="black",label="Data point")
plt.xlabel("Weeks")
plt.ylabel("Sales")
plt.title("LR Demo")
plt.grid(True,alpha=0.3)
plt.legend(loc='best')
plt.show()