import numpy as np
import matplotlib.pyplot as plt


def metj(A, b, x0, itmax):
    D = np.diag(np.diag(A))
    E = -np.tril(A, -1)
    F = -np.triu(A, +1)
    M = D
    N = (E + F)
    T = np.linalg.solve(M,N)
    c = np.linalg.solve(M,b)

    x = x0
    for it in range(itmax):
        x = np.linalg.inv(D)*(E+F)*x[it] + np.linalg.inv(D)*b
    return x


def metgs(A, b, x0, itmax):
    D = np.diag(np.diag(A))
    E = -np.tril(A, -1)
    F = -np.triu(A, +1)
    M = (D-E)
    N = F
    T = np.linalg.solve(M,N)
    c = np.linalg.solve(M,b)
    x = x0
    for it in range(itmax):
        x = np.linalg.inv(D-F) * (b+ F*x[it])

    return x

    

A = [[2,1,1.01], [1,2,1], [1,1,2]]
b = [4,2,2]
x0  = [0,0,0]

autovalores_jacobi = np.linalg.eig(metj(A,b,x0, 1000))



