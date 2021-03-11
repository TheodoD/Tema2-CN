import sys
import numpy as np
import scipy as scipy
from scipy.linalg import cho_factor, cho_solve

A = np.array([[2.25, 3, 3],
              [3, 9.0625, 13],
              [3, 13, 24]])

C = np.linalg.inv(A)
print('B')
print(C)

B = np.array([9, 35.0625, 61])

diag = []

for i in range(len(A)):
    diag.append(A[i][i])

#A = np.linalg.cholesky(A)
A, low = cho_factor(A, lower=True)


print(A)
print(low)

det = 1
for i in range(len(A)):
    det = det * A[i][i]

det = det**2
print(det)

x = cho_solve((A, low), B)
print(x)


for i in range (len(A)):
    for j in range(i+1, len(A[i])):
        A[i][j] = 0

print('A')
AC = np.matmul(scipy.linalg.inv(A), np.transpose(scipy.linalg.inv(A)))

print(AC-C)
print(scipy.linalg.norm(AC-C))


A = np.matmul(A, np.transpose(A))

print(A)

A = np.matmul(A, x)
A = np.subtract(A,B)

print(scipy.linalg.norm(A) )


