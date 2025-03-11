#Tugas kedua
import numpy as np

a = np.array([1,2,3])
b = np.array([1,2,3])
c = np.array([1,2,3])

for_1 = np.dot(a, np.dot(b,c))
for_2 = np.dot(np.dot(a,b) , c)

print(for_1)
print(for_2)

# print(np.array_equal(a,b))
# print(np.array_equal(b,c))

