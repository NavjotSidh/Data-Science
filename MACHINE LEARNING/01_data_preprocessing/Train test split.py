import pandas as pd
from sklearn.model_selection import train_test_split
data = {
    "Study_Hours": [2, 5, 3, 8, 6, 4, 9, 1, 7, 5,
                    3, 6, 8, 2, 10, 4, 7, 1, 9, 6],
    "Attendance": [60, 85, 70, 95, 90, 75, 98, 50, 92, 80,
                   65, 88, 96, 55, 99, 72, 91, 45, 97, 86],
    "Previous_Score": [45, 70, 55, 88, 80, 60, 92, 35, 85, 72,
                       50, 78, 90, 40, 96, 58, 83, 30, 94, 76],
    "Final_Score": [40, 72, 50, 92, 85, 58, 96, 30, 88, 75,
                    48, 80, 94, 35, 98, 55, 86, 25, 97, 82]
}
df = pd.DataFrame(data)
x=df.drop("Final_Score",axis=1)
y=df["Final_Score"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
# print("X train :",x_train)
print(x_test,y_test)
# print("Y train :",y_train)
