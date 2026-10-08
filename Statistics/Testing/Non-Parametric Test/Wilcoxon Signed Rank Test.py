from scipy.stats import wilcoxon
times = [28, 32, 35, 29, 31, 45, 27, 34, 30, 50]
#Expected 30
diff=[x-30 for x in times]
print(diff)
stat,p_val=wilcoxon(diff,alternative="two-sided")
print(stat)
print(p_val)

if p_val<0.05:
    print("Reject H0")
else:
    print("Fail to Reject H0")