import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\NAVJOT\PYCHARM\CSV\Ipl 2026\matches.csv")

Mean_first_inn=np.mean(df["first_ings_score"])
Median_first_inn=df["first_ings_score"].median()
# print("Mean 1st inn :",Mean_first_inn)
# print("Median 1st inn :",Median_first_inn)

Mean_second_inn=np.mean(df["second_ings_score"])
Median_second_inn=df["second_ings_score"].median()
# print("Mean 2nd inn :",Mean_second_inn)
# print("Median 2nd inn :",Median_second_inn)

#Measure of Dispersion
Std_first_inn=df["first_ings_score"].std()
Std_second_inn=df["second_ings_score"].std()
# print(Std_first_inn)
# print(Std_second_inn)
Cv_first_inn=(Std_first_inn/Mean_first_inn)*100
Cv_second_inn=(Std_second_inn/Mean_second_inn)*100
# print("CV in first inn :",Cv_first_inn)
# print("CV in second inn :",Cv_second_inn)

# 5 Number Summary
Min_first_inn=df["first_ings_score"].min()
Q1_first_inn=df["first_ings_score"].quantile(0.25)
Q3_first_inn=df["first_ings_score"].quantile(0.75)
Max_first_inn=df["first_ings_score"].max()

Min_second_inn=df["second_ings_score"].min()
Q1_second_inn=df["second_ings_score"].quantile(0.25)
Q3_second_inn=df["second_ings_score"].quantile(0.75)
Max_second_inn=df["second_ings_score"].max()

#Outliers
iqr_first_inn=Q3_first_inn-Q1_first_inn
lf_first_inn=Q1_first_inn- 1.5 * iqr_first_inn
uf_first_inn=Q3_first_inn + 1.5 * iqr_first_inn
print(lf_first_inn,uf_first_inn)

iqr_second_inn=Q3_second_inn-Q1_second_inn
lf_second_inn=Q1_second_inn- 1.5 * iqr_second_inn
uf_second_inn=Q3_second_inn + 1.5 * iqr_second_inn
print(lf_second_inn,uf_second_inn)

outlies_first_inn=df[(df["first_ings_score"]< lf_first_inn) | (df["first_ings_score"]>uf_first_inn) ]
outlies_second_inn=df[(df["second_ings_score"]< lf_second_inn) | (df["second_ings_score"]>uf_first_inn) ]
print("Outliers in first inn :",outlies_first_inn["first_ings_score"])
print("Outliers in second inn :",outlies_second_inn["second_ings_score"])