import numpy as np


r, c = map(int, input().split())
i = np.array([input().split() for _ in range(r)],int)
tra = np.transpose(i)
flatened = i.flatten()