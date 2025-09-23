import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import scienceplots
from matplotlib.ticker import FuncFormatter

inch = 0.0393700787
fig_width = 180 * inch #in inch
fig_height = 3 # in inch

min_nstress = 0
max_nstress = 7
min_sstress = 0
max_sstress = 3
plt.style.use(["science","ieee"])


def format_ticks(x, pos):
    if x.is_integer():
        return f'{int(x)}'
    else:
        return f'{x:.1f}'

data = "data/JSC_dried_1runs_20250709.xlsx"

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
    

ax.axhline(6, 0, (310/60)/18, color = "tab:blue", linestyle = "dotted")
ax.axhline(6, (460/60)/18,(590/60)/18, color = "tab:blue", linestyle = "dotted")
ax.axhline(6, (740/60)/18, (905/60)/18, color = "tab:blue", linestyle = "dotted")

ax.axvline(310/60, (1849.4/1000)/7 , 6/7, color = "tab:blue", linestyle = "dashed")
ax.axvline(460/60, (1849/1000)/7, 6/7, color = "tab:blue", linestyle = "dashed")
ax.axvline(590/60, (3295.2/1000)/7, 6/7, color = "tab:blue", linestyle = "dashed")
ax.axvline(740/60, (3295.2/1000)/7, 6/7, color = "tab:blue", linestyle = "dashed")
ax.axvline(905/60, (4769.3/1000)/7, 6/7, color = "tab:blue", linestyle = "dashed")


ax2.plot(400/60, 744.63/1000, marker = "x", color = "tab:red")
ax2.plot(683.6/60, 1117.4/1000, marker = "x", color = "tab:red")
ax2.plot(992.9/60, 1454.1/1000, marker = "x", color = "tab:red")


ax.set_xlabel(r"t [min]")
ax.set_ylim(min_nstress,max_nstress)
ax.set_xlim(0,18)
ax.set_yticks(np.arange(0,8,1))
ax.set_ylabel(r"Normal Stress $\sigma_n \ $[kPa]", color = "tab:blue")
ax.yaxis.set_major_formatter(FuncFormatter(format_ticks))

ax2.set_ylabel(r"Shear Stress $\tau \ $[kPa]", color = "tab:orange")
ax2.set_yticks(np.arange(0,3.1,0.5))
ax2.set_ylim(min_sstress,max_sstress)
ax2.yaxis.set_major_formatter(FuncFormatter(format_ticks))

plt.savefig("jsc_dried_6kPa.svg", dpi=300, bbox_inches='tight')







