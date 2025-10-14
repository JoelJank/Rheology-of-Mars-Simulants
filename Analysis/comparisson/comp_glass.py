import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce

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

dried = plt.plot(sorted(flatten([dried3kPa_ns, dried6kPa_ns, dried9kPa_ns])), sorted(flatten([dried3kPa_ss, dried6kPa_ss, dried9kPa_ss])), 'o--', label='3, 6, 9 kPa dried', marker = "None")
plt.plot(dried3kPa_ns, dried3kPa_ss, 'o', color = dried[0].get_color(), linestyle = "None")
plt.plot(dried6kPa_ns, dried6kPa_ss, 'v', color = dried[0].get_color(), linestyle = "None")
plt.plot(dried9kPa_ns, dried9kPa_ss, 'h', color = dried[0].get_color(), linestyle = "None")
plt.plot(sorted(flatten([ w10per6kPa_ns, w10per9kPa_ns])), sorted(flatten([ w10per6kPa_ss, w10per9kPa_ss])), 'o--', label=' 6, 9 kPa 10$\%$ water')
plt.plot(sorted(flatten([w20per3kPa_ns, w20per6kPa_ns, w20per9kPa_ns])), sorted(flatten([w20per3kPa_ss, w20per6kPa_ss, w20per9kPa_ss])), 'o--', label='3, 6, 9 kPa $20\%$ water')
plt.plot(p15dried_ns, p15dried_ss, 'o-', label='15 kPa dried')
plt.plot(p15driedall_ns, p15driedall_ss, 'o-', label='Full dried')
plt.plot(p15w5per_ns, p15w5per_ss, 'o-', label=r'15 kPa 5$\%$ water')
plt.plot(p15w15per_ns, p15w15per_ss, 'o-', label=r'15 kPa 15$\%$ water')
plt.plot(p15w25per_ns, p15w25per_ss, 'o-', label=r'15 kPa 25$\%$ water')
plt.plot(hanley_data['ns'][:5], hanley_data['ss'][:5], color = 'lightgray', label='Hanley et al. (2015)', linestyle = "None" , marker = 'D')
plt.xlabel("Normal Stress (Pa)")
plt.ylabel("Shear Stress (Pa)")
plt.legend(loc='upper left')
plt.grid()
plt.savefig("Mohr_Coulomb_All_Glass.svg", dpi=300)