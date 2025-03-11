import numpy as np

# def chauchy_schwarg(u,v):
#     #Dot product
#     dot_product = np.dot(u,v)

#     #hitung norma
#     norm_u = np.linalg.norm(u)
#     norm_v = np.linalg.norm(v)

#     #cek
#     return abs(dot_product) <= (norm_u)*(norm_v)

# def hitung_panjang(u,v):
#     x = np.linalg.norm(u)
#     y = np.linalg.norm(v)
#     return x,y

# a = np.array([3,-2,2])
# b = np.array([1,4,-3])
# hasil = chauchy_schwarg(a,b)
# hasilp = hitung_panjang(a,b)

# print(f"hasilnya adlah: {hasil}")
# print

#Vectors
a = np.array([-3,4,5])
b = np.array([3,6,-3])

#skalars

s1 = np.array(5)
s2 = np.array(9)
dps = np.dot(s1,s2)
#Dot product with vectors
dp_1 = np.dot(a,b)
dp_2 = np.dot(a*s1,b*s2)

#PRint
print(dp_2)