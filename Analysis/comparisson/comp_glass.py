import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
from functools import reduce
import scipy.stats

plt.style.use('paper.mplstyle')
def flatten(l):
    return list(reduce(lambda x, y: x + y, l, []))


hanley_data = pd.read_csv('Hanley et al\dryglass.csv', header = None, names = ["ns", "ss"], sep = ';')
print(hanley_data)


dried3kPa_ns = [825.06991984, 1607.13346693, 2338.56472946]
dried3kPa_ss = [348.77485714, 442.64571429, 558.05571429]
dried6kPa_ns = [1689.12945892, 3284.09058116, 4718.03527054]
dried6kPa_ss = [447.81342857, 688.50828571, 882.88571429]
dried9kPa_ns = [2664.76513026, 4930.89378758, 7155.19659319]
dried9kPa_ss = [637.16828571, 944.46142857, 1276.648]
w20per3kPa_ns = [995.94004008, 1781.82004008, 2347.44328657]
w20per3kPa_ss = [707.77628571, 784.20685714, 893.24057143]
w20per6kPa_ns = [1885.60480962, 3243.53687375, 4643.01382766]
w20per6kPa_ss = [902.53085714, 986.36457143, 1252.74571429]
w20per9kPa_ns = [2745.69859719, 5014.149499, 7107.20200401]
w20per9kPa_ss = [1153.16, 1479.58, 1808.95428571]
p15dried_ns = [5956.24606365, 6658.79432387,  7417.80317195,  8245.42804674,  9003.68814691,  9758.04357262, 10509.79298831, 11255.70617696,  12006.319933]
p15dried_ss = [1108.49142857, 1091.08657143, 1306.81142857, 1723.24857143, 2285.14,  2844.44857143, 3283.98285714, 3594.54285714, 4061.66857143]
p15driedall_ns = [1969.40267559,  3951.93522538,  6479.09048414,  8494.56193656, 10011.08831386, 11802.20367279, 13511.09866221]
p15driedall_ss = [580.96285714,  792.24028571, 1186.73428571, 2027.14571429, 2929.93714286,3844.09142857, 4955.52]
p15w5per_ns = [6028.219933, 6748.13472454,  7453.27746244,  8257.18297162,  9009.67813022,  9759.10584307, 10511.33055092, 11254.61936561,  12019.6281407]
p15w5per_ss = [1353.85142857, 1499.53142857, 1611.24571429, 2154.47142857, 2592.22571429,  3169.92571429, 3528.23142857, 3943.48, 4575.13142857]
p15w15per_ns = [6014.65745394,  6764.57095159,  7465.90751252,  8258.53789649,  9008.60901503,  9756.47762938, 10504.16360601, 11256.30050083,  12013.86432161]
p15w15per_ss = [1409.93714286, 1613.53142857, 1743.22857143, 2172.91142857, 2709.37142857,  3181.73428571, 3511.42857143, 3965.61714286, 4638.34285714]
p15w25per_ns = [6041.01574539,  6787.85108514,  7475.76010017,  8269.01919866,  9021.4345576,   9757.29048414, 10503.82470785, 11260.64774624,  12009.44053601]
p15w25per_ss = [1647.15428571, 2001.24285714, 1869.37428571, 2489.00285714, 3011.92,  3815.8,  4333.25142857, 4691.33142857, 5355.27142857]
w10per3kPa_ns = [952.0611022,  1694.24709419, 2419.73266533]
w10per3kPa_ss = [727.32314286, 776.49057143, 780.45685714]
w10per6kPa_ns = [1857.8507014,  3295.46933868, 4760.22645291]
w10per6kPa_ss = [789.33685714,  950.62, 1145.53714286]
w10per9kPa_ns = [2758.4242485,  5011.73667335, 7138.44488978]
w10per9kPa_ss = [984.92257143, 1266.84, 1539.59428571]

x = np.linspace(0, sorted(flatten([dried3kPa_ns, dried6kPa_ns, dried9kPa_ns]))[-1],1000)
x10 = np.linspace(0, sorted(flatten([ w10per6kPa_ns, w10per9kPa_ns]))[-1],1000)
x20 = np.linspace(0, sorted(flatten([ w20per3kPa_ns, w20per6kPa_ns, w20per9kPa_ns]))[-1],1000)
xhanley = np.linspace(0, hanley_data['ns'][4], 1000)

def lin_fit(x, slope, intercept):
    return slope * x + intercept

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(sorted(flatten([dried3kPa_ns, dried6kPa_ns, dried9kPa_ns, p15driedall_ns[0:3],p15dried_ns[0:3]])), sorted(flatten([dried3kPa_ss, dried6kPa_ss, dried9kPa_ss, p15driedall_ss[0:3],p15dried_ss[0:3]])))
dried = plt.plot(x,lin_fit(x, slope, intercept), linestyle = '-', label=f'dried, $R^2 = {round(r_value,3)}$', marker = "None", color = '#BAE6FD')
plt.plot(dried3kPa_ns, dried3kPa_ss, 'o', color = dried[0].get_color(), linestyle = "None")
plt.plot(dried6kPa_ns, dried6kPa_ss, 'v', color = dried[0].get_color(), linestyle = "None")
plt.plot(dried9kPa_ns, dried9kPa_ss, 'h', color = dried[0].get_color(), linestyle = "None")
plt.plot(p15w5per_ns[2:], p15w5per_ss[2:], 's', color = '#7DD3FC', alpha = 0.5, linestyle = ":")
plt.plot(p15w5per_ns[0:3], p15w5per_ss[0:3], 's-', label=r'5$\%$ water', color = '#7DD3FC')
plt.plot(p15driedall_ns[:3], p15driedall_ss[:3], 's', color = dried[0].get_color(), linestyle = "None")
plt.plot(p15dried_ns[:3], p15dried_ss[:3], 's', color = dried[0].get_color(), linestyle = "None")
slope10,intercept10, r_value10, p_value10, std_err10 = scipy.stats.linregress(sorted(flatten([w10per6kPa_ns, w10per9kPa_ns])), sorted(flatten([w10per6kPa_ss, w10per9kPa_ss])))
ten_percent = plt.plot(x10,lin_fit(x10,slope10, intercept10), linestyle = '-', label=f'10$\%$ water, $R^2 = {round(r_value10,3)}$', marker = "None", color = '#60A5FA')
plt.plot(w10per6kPa_ns, w10per6kPa_ss, 'v', color = ten_percent[0].get_color(), linestyle = "None")
plt.plot(w10per9kPa_ns, w10per9kPa_ss, 'h', color = ten_percent[0].get_color(), linestyle = "None")
plt.plot(p15w15per_ns[2:], p15w15per_ss[2:], 's', color = '#3B82F6', alpha = 0.5, linestyle = ":")
plt.plot(p15w15per_ns[0:3], p15w15per_ss[0:3], marker = 's', linestyle = '-', label=r'15$\%$ water', color = '#3B82F6')
slope20, intercept20, r_value20, p_value20, std_err20 = scipy.stats.linregress(sorted(flatten([w20per3kPa_ns, w20per6kPa_ns, w20per9kPa_ns])), sorted(flatten([w20per3kPa_ss, w20per6kPa_ss, w20per9kPa_ss])))
twenty_per = plt.plot(x20, lin_fit(x20, slope20, intercept20), linestyle = '-', label=f'20$\%$ water, $R^2 = {round(r_value20,3)}$', marker = "None", color = '#1E3A8A')
plt.plot(w20per3kPa_ns, w20per3kPa_ss, 'o', color = twenty_per[0].get_color(), linestyle = "None")
plt.plot(w20per6kPa_ns, w20per6kPa_ss, 'v', color = twenty_per[0].get_color(), linestyle = "None")
plt.plot(w20per9kPa_ns, w20per9kPa_ss, 'h', color = twenty_per[0].get_color(), linestyle = "None")
plt.plot(p15w25per_ns[2:], p15w25per_ss[2:], 's', color = '#000080', alpha = 0.5, linestyle = ":")
plt.plot(p15w25per_ns[0:3], p15w25per_ss[0:3], 's-', label=r'25$\%$ water', color = '#000080')
slopehanley, intercepthanley, r_valuehanley, p_valuehanley, std_errhanley = scipy.stats.linregress(hanley_data['ns'][:4], hanley_data['ss'][:4])
plt.plot(xhanley, lin_fit(xhanley, slopehanley, intercepthanley),linestyle = '-', label = f'Hanley et al. (2015)', marker = "None", color = 'lightgray')
plt.plot(hanley_data['ns'][:4], hanley_data['ss'][:4], color = 'lightgray', linestyle = "None" , marker = 'D')
plt.plot(sorted(flatten([p15driedall_ns[3:],p15dried_ns[2:]])), sorted(flatten([p15driedall_ss[3:],p15dried_ss[2:] ])), 's', color = '#BAE6FD', alpha = 0.5, linestyle = ":")
plt.axvline(x = 7800, color = 'k', linestyle = '--')
plt.axvspan(0,7800, color = '#DAA520',alpha = 0.8)
plt.axvspan(7800,14000, color = '#6B8E23',alpha = 0.5)
plt.xlabel("Normal Stress (Pa)")
plt.ylabel("Shear Stress (Pa)")
handles =[Line2D([0], [0], color=dried[0].get_color(),linestyle = '-'),
          Line2D([0], [0], color='#7DD3FC',linestyle = '-'),
          Line2D([0], [0], color=ten_percent[0].get_color(),linestyle = '-'),
          Line2D([0], [0], color='#3B82F6',linestyle = '-'),
          Line2D([0], [0], color=twenty_per[0].get_color(),linestyle = '-'),
          Line2D([0], [0], color='#000080',linestyle = '-'),
          Line2D([0], [0], color='lightgray',linestyle = '-'),
]
labels = ['dried', '5\% water', '10\% water', '15\% water', '20\% water', '25\% water', 'Hanley et al. (2015)']
legend = plt.legend(
    handles = handles,
    labels = labels,
    loc='center left',
    frameon=True,
    fontsize=8,   
    borderpad=0.2 
)
frame = legend.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('black')
frame.set_linewidth(1.0)
frame.set_alpha(1)
legend.set_zorder(10) 
plt.text(3900, 6500, "Region 1", ha='center', va='center', fontsize = 20, color = 'black')
plt.text(10900, 6500, "Region 2", ha='center', va='center', fontsize = 20, color = 'black')
plt.grid()
plt.xlim(0,14000); plt.ylim(0,7100)
plt.savefig("Mohr_Coulomb_All_Glass.svg", dpi=300)