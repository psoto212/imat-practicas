import numpy as np
from ej_4 import *
import matplotlib.pyplot as plt


def parametro_arco(xp, yp):
    xp = np.asarray(xp, dtype=float)
    yp = np.asarray(yp, dtype=float)
    dx = np.diff(xp)
    dy = np.diff(yp)
    ds = np.sqrt(dx*dx + dy*dy)
    t = np.zeros(len(xp), dtype=float)
    t[1:] = np.cumsum(ds)

    return t


def dibujar_spline_parametrico(xp, yp, N=800):
    xp = np.asarray(xp, dtype=float)
    yp = np.asarray(yp, dtype=float)

    if len(xp) != len(yp):
        raise ValueError('xp e yp deben tener la misma longitud.')
    if len(xp) < 2:
        raise ValueError('Necesitas al menos 2 puntos.')

    t = parametro_arco(xp, yp)

    Sx, Mx = spline_cubico_natural(t, xp)
    Sy, My = spline_cubico_natural(t, yp)

    tt = np.linspace(t[0], t[-1], N)
    xx = Sx(tt)
    yy = Sy(tt)

    plt.figure()
    plt.plot(xx, yy, color='darkgreen', label='Spline (x(t), y(t))')
    plt.plot(xp, yp, 'o', color='limegreen', label='Puntos medidos')
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.title('Spline cúbico')
    plt.show()

    return t, (Sx, Sy), (Mx, My)

if __name__ == '__main__':
    xp = [-3.7, -2, -1.2, -0.6, 0.7, 1.8, 2.7, 3.4, 3.6, 3.9]
    yp = [ 0.4, 3.9,  3.9,  4.8, 4.8, 4.3, 3.8, 2.4, 1.2, 0.0]

    dibujar_spline_parametrico(xp, yp)   