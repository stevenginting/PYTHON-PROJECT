import numpy as np

a = np.random.randint(100)
b = np.random.randint(100)

f_1 = np.dot(a,b)
f_2 = np.dot(b,a)
print(f_1,f_2, f_1 - f_2)