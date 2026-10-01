import numpy as np

def momentos_spline_natural(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    n = len(x) - 1
    if n < 1:
        raise ValueError('Necesitas al menos 2 nodos.')
    if np.any(np.diff(x) <= 0):
        raise ValueError('x debe ser estrictamente creciente.')
    h = np.diff(x)
    if n == 1:
        return np.zeros(2)
    m = n - 1
    A = np.zeros((m, m))
    d = np.zeros(m)

    for j in range(1, n):  
        hj   = h[j-1]
        hj1  = h[j]
        lam = hj1 / (hj + hj1)
        mu  = hj  / (hj + hj1)
        dj = (6.0 / (hj + hj1)) * ((y[j+1]-y[j])/hj1 - (y[j]-y[j-1])/hj)
        row = j - 1
        A[row, row] = 2.0
        d[row] = dj
        if row - 1 >= 0:
            A[row, row - 1] = mu
        if row + 1 < m:
            A[row, row + 1] = lam

    M_interior = np.linalg.solve(A, d)
    M = np.zeros(n + 1)
    M[1:n] = M_interior
    return M


def spline_cubico_natural(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    M = momentos_spline_natural(x, y)
    h = np.diff(x)

    def S(z):
        z = np.asarray(z)
        j = np.searchsorted(x, z, side='right') - 1
        j = np.clip(j, 0, len(x) - 2)
        dx = z - x[j]
        hj = h[j]
        term1 = (M[j+1] - M[j]) * (dx**3) / (6.0 * hj)
        term2 = (M[j] / 2.0) * (dx**2)
        term3 = ((y[j+1]-y[j]) / hj - (2.0*M[j] + M[j+1]) * hj / 6.0) * dx
        return term1 + term2 + term3 + y[j]

    return S, M


