import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import pandas as pd
from functools import reduce

plt.style.use('paper.mplstyle')
def flatten(l):
    return list(reduce(lambda x, y: x + y, l, []))

def linregress_with_uncerainty(x,y):
    
    slope,intercept, r_value, p_value, std_err = scipy.stats.linregress(x,y)
    
    n = len(x)
    x_arr = np.array(x)
    y_arr = np.array(y)
    
    y_fit = slope * x_arr + intercept
    residuals = y_arr - y_fit
    mse = np.sum(residuals**2) / (n - 2)
    
    x_mean = np.mean(x_arr)
    s_xx = np.sum((x_arr - x_mean)**2)
    
    slope_uncertainty = np.sqrt(mse / s_xx)
    intercept_uncertainty = np.sqrt(mse * (1/n + x_mean**2 / s_xx))
    
    return [slope, intercept, slope_uncertainty, intercept_uncertainty, r_value, p_value, std_err]



dried_ns = sorted([825.06991984, 1607.13346693, 2338.56472946, 1689.12945892, 3284.09058116, 4718.03527054,2664.76513026, 4930.89378758, 7155.19659319,1969.40267559,  3951.93522538,  6479.09048414,5956.24606365, 6658.79432387,  7417.80317195])
dried_ss = sorted([348.77485714, 442.64571429, 558.05571429,447.81342857, 688.50828571, 882.88571429,637.16828571, 944.46142857, 1276.648,580.96285714,  792.24028571, 1186.73428571,1108.49142857, 1091.08657143, 1306.81142857])
w5_ns = [6028.219933, 6748.13472454,  7453.27746244]
w5_ss = [1353.85142857, 1499.53142857, 1611.24571429]
w10_ns = sorted([1857.8507014,  3295.46933868, 4760.22645291,2758.4242485,  5011.73667335, 7138.44488978])
w10_ss = sorted([789.33685714,  950.62, 1145.53714286, 984.92257143, 1266.84, 1539.59428571])
w15_ns = [6014.65745394,  6764.57095159,  7465.90751252]
w15_ss = [1409.93714286, 1613.53142857, 1743.22857143]
w20_ns = sorted([995.94004008, 1781.82004008, 2347.44328657,1885.60480962, 3243.53687375, 4643.01382766,2745.69859719, 5014.149499, 7107.2020040])
w20_ss = sorted([707.77628571, 784.20685714, 893.24057143,902.53085714, 986.36457143, 1252.74571429, 1153.16, 1479.58, 1808.95428571])
w25_ns = [6041.01574539,  6787.85108514,  7475.76010017]
w25_ss = [1647.15428571, 2001.24285714, 1869.37428571]

dried = linregress_with_uncerainty(dried_ns, dried_ss)
w5 = linregress_with_uncerainty(w5_ns, w5_ss)
w10 = linregress_with_uncerainty(w10_ns, w10_ss)
w15 = linregress_with_uncerainty(w15_ns, w15_ss)
w20 = linregress_with_uncerainty(w20_ns, w20_ss)
w25 = linregress_with_uncerainty(w25_ns, w25_ss)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

ax1.errorbar(np.array([0,0.05,0.1,0.15,0.2,0.25]), np.array([dried[1], w5[1], w10[1], w15[1], w20[1], w25[1]])/100, yerr = np.array([dried[3], w5[3], w10[3], w15[3], w20[3], w25[3]])/100, marker = 'o', color = 'tab:blue', capsize = 3, linestyle = '-', markersize = 3)
ax1.set_xlim(0,0.3)
ax1.set_xlabel("Water content")
ax1.set_ylabel("$\sigma_c [Pa]$")
ax2.plot(np.array([0,0.05,0.1,0.15,0.2,0.25]), np.array([dried[0], w5[0], w10[0], w15[0], w20[0], w25[0]]), marker = 'o', color = 'tab:orange', linestyle = '-', markersize = 3)
plt.show()