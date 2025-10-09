import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

data = "H:/AG Parteli\Paris\Rheology-of-Mars-Simulants/Analysis/raw_data/Excel/Glass_15kPa/Glass_15kPa.xlsx"

df = pd.read_excel(data,  sheet_name = "20250923G0p25", 
                   header = None,
                   names = ["No", "Time", "Gap", "NormForce", "NormStress", "Torque", "ShearStress", "RotSpeed"],
                   skiprows=3).dropna()

mask = df.apply(lambda row: any(isinstance(x, str) for x in row), axis=1)
df = df[~mask].dropna().reset_index(drop=True)

jumps_where = np.array([0])

num_col = df["No"].values
jumps_where_list = np.add(np.where(np.abs(np.diff(num_col)) > 10)[0], 1)
jumps_where = np.append(jumps_where,jumps_where_list)
sections = [df.iloc[jumps_where[i]:jumps_where[i+1]].reset_index(drop=True) for i in range(len(jumps_where)-1)]

filtered_sections = [
    section for section in sections
    if len(section) >= 25
    and not ((section["NormStress"] >= 14500) & (section["NormStress"] <= 15500)).any()
]

result_df = pd.concat(filtered_sections, ignore_index= True)

plt.plot(result_df["Time"]/60,result_df["NormStress"], color = "blue")
plt.plot(result_df["Time"]/60, result_df["ShearStress"], color = "red")
plt.savefig("test.png", dpi=300)

result_df.to_excel("H:/AG Parteli/Paris/Rheology-of-Mars-Simulants/Analysis/raw_data/Excel/Glass_15kPa/Glass_25percentwater.xlsx", index = False)


