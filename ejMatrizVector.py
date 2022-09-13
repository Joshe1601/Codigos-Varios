import numpy as np

# A = np.array([1,2,3,4])
# print(A)
# A_M = np.reshape(A, [2,2])
# print("\n", A_M)
# print("\n", A_M[0][0])
# v = np.array([1,2])
# print("\n", v)
# b = A_M.dot(v)
# print(b)


A = [1, 2, 3, 4]
v = [1,2]

b = []
suma = 0

for i in range(len(v)):
    for j in range(len(A)):
        suma += A[i+j]*v[j]
        b.append(suma)

print(b)



