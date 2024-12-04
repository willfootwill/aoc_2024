import pandas as pd
import numpy as np

data = pd.read_csv('~/github/aoc_2024/input/day1', header=None, sep=r'\s+')
df = pd.DataFrame(data)
df[:] = np.sort(df.values, axis=0)
df["delta"] = abs(df[0] - df[1])
print(sum(df["delta"]))


same_map = dict(df[1].value_counts())
df["similar"] = df[0].apply(lambda x: x * same_map.get(x,0))
print(sum(df["similar"]))