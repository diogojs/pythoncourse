import numpy as np
from datetime import datetime


def manual_product(a, b):
    result = 0
    for e, f in zip(a, b):
        result += e*f
    return result


a = np.random.randn(100)
b = np.random.randn(100)
T = 100000

t0 = datetime.now()
for t in range(T):
    manual_product(a, b)
dt0 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
    a.dot(b)
dt1 = datetime.now() - t0

print("dt0/dt1 = ", dt0.total_seconds() / dt1.total_seconds())
