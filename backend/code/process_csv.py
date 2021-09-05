import pandas as pd
import numpy as np

sdr_df = pd.read_csv("./datasets/CSV/sym_dis_rel.csv")
s_df = pd.read_csv("./datasets/CSV/sym.csv")
d_df = pd.read_csv("./datasets/CSV/dis.csv")

df = pd.DataFrame(columns=s_df["Symptom Term"],index=d_df["Disease Term"])
sdr_df = sdr_df[["Symptom Term","Disease Term"]]

for ind,row in sdr_df.iterrows():
	df.loc[row["Disease Term"], row["Symptom Term"]] = 1

df.fillna(0,inplace=True)

df.to_csv("./datasets/CSV/clean.csv")