import numpy as np

a = np.random.randn(4,6)
b = np.random.randn(4,6)

print(a)
print('')
print(b)

dps = np.zeros(6)
for i in range(6):
    dps[i] = np.dot (a[:,i],b[:,i])

print('')
print(dps)

