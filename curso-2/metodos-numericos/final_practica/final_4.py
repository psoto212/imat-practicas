import numpy as np
import matplotlib.pyplot as plt




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





