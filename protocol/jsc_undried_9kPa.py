import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import scienceplots
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Circle

inch = 0.0393700787
fig_width = 180 * inch #in inch
fig_height = 3 # in inch

min_nstress = 0
max_nstress = 10
min_sstress = 0
max_sstress = 4
plt.style.use(["science","ieee"])


def format_ticks(x, pos):
    if x.is_integer():
        return f'{int(x)}'
    else:
        return f'{x:.1f}'

data = "data/JSC_undried_2runs_20250708.xlsx"

fig, ax = plt.subplots(figsize=(fig_width,fig_height))
ax2 = ax.twinx()


for i in range (1,4):
    df = pd.read_excel(
        data,
        sheet_name= f"{i}",
        header = None,
        names = ["Point No.", "Time", "Gap", "Normal Force","Normal Stress","Torque","Shear Stress","Rotational Speed"],
        skiprows=3).dropna()
    ax.plot(df["Time"]/60, df["Normal Stress"]/1000, color = "tab:blue", linestyle = "solid")
    ax2.plot(df["Time"]/60, df["Shear Stress"]/1000, color = "tab:orange", linestyle = "solid")
    
ax.axhline(9, 0, (160/60)/15.5, color = "tab:blue", linestyle = "dotted")
ax.axhline(9, (310/60)/15.5,(440/60)/15.5, color = "tab:blue", linestyle = "dotted")
ax.axhline(9, (590/60)/15.5, (760/60)/15.5, color = "tab:blue", linestyle = "dotted")

ax.axvline(160/60, (2679/1000)/10 , 9/10, color = "tab:blue", linestyle = "dashed")
ax.axvline(310/60, (2679/1000)/10, 9/10, color = "tab:blue", linestyle = "dashed")
ax.axvline(440/60, (4900/1000)/10, 9/10, color = "tab:blue", linestyle = "dashed")
ax.axvline(590/60, (4900/1000)/10, 9/10, color = "tab:blue", linestyle = "dashed")
ax.axvline(760/60, (7200/1000)/10, 9/10, color = "tab:blue", linestyle = "dashed")


ax2.plot(267.1/60, 1137.8/1000, marker = "x", color = "tab:red")
ax2.plot(545.9/60, 1581/1000, marker = "x", color = "tab:red")
ax2.plot(866.2/60, 2019/1000, marker = "x", color = "tab:red")

ax.set_xlabel(r"t [min]")
ax.set_ylim(min_nstress,max_nstress)
ax.set_xlim(0,15.5)
ax.set_yticks(np.arange(0,11,1))
ax.set_ylabel(r"Normal Stress $\sigma_n \ $[kPa]", color = "tab:blue")
ax.yaxis.set_major_formatter(FuncFormatter(format_ticks))

ax2.set_ylabel(r"Shear Stress $\tau \ $[kPa]", color = "tab:orange")
ax2.set_yticks(np.arange(0,4.5,0.5))
ax2.set_ylim(min_sstress,max_sstress)
ax2.yaxis.set_major_formatter(FuncFormatter(format_ticks))

plt.savefig("jsc_undried.svg", dpi=300, bbox_inches='tight')







