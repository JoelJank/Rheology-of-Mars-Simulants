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
max_nstress = 10
min_sstress = 0
max_sstress = 4
plt.style.use(["science","ieee"])


def format_ticks(x, pos):
    if x.is_integer():
        return f'{int(x)}'
    else:
        return f'{x:.1f}'

data = "data/JSC_dried.xlsx"

fig, ax = plt.subplots(figsize=(fig_width,fig_height))
ax2 = ax.twinx()

full_df = pd.read_excel(
    data,
    sheet_name= "Feuil1",
    header = None,
    names = ["Point No.", "Time", "Gap", "Normal Force","Normal Stress","Torque","Shear Stress","Rotational Speed"],
    skiprows=2).dropna()


for i in range(1,13):
    
    df = pd.read_excel(
        data, 
        sheet_name= f"{i}", 
        header = None, 
        names = ["Point No.", "Time", "Gap", "Normal Force","Normal Stress","Torque","Shear Stress","Rotational Speed"], 
        skiprows=2).dropna()
    
    ax.plot(df["Time"]/60, df["Normal Stress"]/1000, color = 'tab:blue', linestyle= 'solid')
    
ax2.plot(full_df["Time"]/60, full_df["Shear Stress"]/1000, color = 'tab:red', linestyle = 'solid')

ax.axvline(130/60, (2675.1/1000)/(max_nstress-min_nstress), (9018.1/1000)/(max_nstress-min_nstress), color = "tab:blue", linestyle = "dashed")
ax.axvline(300/60, (2699.5/1000)/(max_nstress-min_nstress), (8950.5/1000)/(max_nstress-min_nstress), color = 'tab:blue', linestyle = 'dashed')
ax.axvline(500/60, (4904.7/1000)/(max_nstress-min_nstress), (8999/1000)/(max_nstress-min_nstress), color = 'tab:blue', linestyle = 'dashed')
ax.axvline(670/60, (4929.3/1000)/(max_nstress-min_nstress), (8969.4/1000)/(max_nstress-min_nstress), color = 'tab:blue', linestyle = 'dashed')
ax.axvline(795/60, (7262.2/1000)/(max_nstress-min_nstress), (9029.2/1000)/(max_nstress-min_nstress), color = 'tab:blue', linestyle = 'dashed')

ax.set_xlabel(r"t [min]")
ax.set_ylim(min_nstress,max_nstress)
ax.set_xlim(0,16.5)
ax.set_yticks(np.arange(0,11,1))
ax.set_ylabel(r"Normal Stress $\sigma_n \ $[kPa]")
ax.yaxis.set_major_formatter(FuncFormatter(format_ticks))



ax2.set_ylabel(r"Shear Stress $\tau \ $[kPa]")
ax2.set_yticks(np.arange(0,4.5,0.5))
ax2.set_ylim(min_sstress,max_sstress)
ax2.yaxis.set_major_formatter(FuncFormatter(format_ticks))


plt.savefig("plot.svg", dpi=300, bbox_inches='tight')





