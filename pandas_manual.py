# Section 2
# Manual Data Loading

import numpy as np

X = []

for line in open("./data/data_2d.csv"):
    row = line.split(',')
    sample = list(map(float, row))
    X.append(sample)

X = np.array(X)
print(X.shape)
