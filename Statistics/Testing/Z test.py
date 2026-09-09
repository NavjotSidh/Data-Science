u=100
from statsmodels.stats.weightstats import ztest
data=[88,92,94,94,96,97,97,99,99,105,109,109,109,109,110,112,112,113,114,115]
z_stat, p_value = ztest(data,value=110)

print("Z-statistic:", z_stat)
print("P-value:", p_value)