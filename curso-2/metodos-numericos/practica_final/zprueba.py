import numpy as np


def coef_indet(x, A, b):
    n = len(x)
    A = np.zeros((n, n))
    v = np.zeros(n)

    for j in range(n):
        A[j, :] = x**j

        v[j] = (b[j+1] - a[j+1])/(j+1)


    c = np.linalg.solve(A,v)

    return c


exacta = np.log(2)
