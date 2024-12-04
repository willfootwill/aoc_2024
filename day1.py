import pandas as pd
import numpy as np

df = pd.read_csv('~/github/aoc_2024/input/day1', header=None, sep=r'\s+')
df[:] = np.sort(df.values, axis=0)
df["delta"] = abs(df[0] - df[1])
print(sum(df["delta"]))