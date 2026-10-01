import numpy as np
#ejercicio 3d
def cholesky(A):
    A = np.array(A, dtype=float)
    n = A.shape[0]
    C = np.zeros((n, n))

    for j in range(n):
        suma = 0.0
        for k in range(j):
            suma += C[j, k]**2
        C[j, j] = np.sqrt(A[j, j] - suma)

        for i in range(j + 1, n):
            suma = 0.0
            for k in range(j):
                suma += C[i, k] * C[j, k]
            C[i, j] = (A[i, j] - suma) / C[j, j]

    return C



#ejercicio 3e

A = np.array([[6, 15, 55],
              [15, 55, 225],
              [55, 225, 979]], dtype=float)

b = np.array([100, 150, 100], dtype=float)

C = cholesky(A)
y = np.linalg.solve(C, b)
x = np.linalg.solve(C.T, y)

print("La solución del sistema es:")
print(x)