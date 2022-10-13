import numpy as np

z = np.zeros(20)
z.shape = (4,5)

print(z.shape)

for i in range(4):
    for j in range(5):
        z[i][j] = i

print(z)
