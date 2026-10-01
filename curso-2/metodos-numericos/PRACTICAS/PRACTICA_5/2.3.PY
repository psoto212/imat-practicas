import numpy as np


def biseccion(f, a, b, tolerancia=1e-6, iteraciones=100):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a
    if fb == 0:
        return b
    if fa * fb > 0:
        raise ValueError("No hay cambio de signo en [a,b].")

    for _ in range(iteraciones):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tolerancia or 0.5 * (b - a) < tolerancia:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return 0.5 * (a + b)


def secante(f, x0, x1, tolerancia=1e-10, iteraciones=100):
    f0 = f(x0)
    f1 = f(x1)

    if abs(f0) < tolerancia:
        return x0
    if abs(f1) < tolerancia:
        return x1

    for _ in range(iteraciones):
        denom = f1 - f0
        if abs(denom) < 1e-14:
            raise ValueError("División por número muy pequeño en secante.")

        x2 = x1 - f1 * (x1 - x0) / denom
        f2 = f(x2)

        if abs(f2) < tolerancia or abs(x2 - x1) < tolerancia:
            return x2

        x0, f0 = x1, f1
        x1, f1 = x2, f2

    return x1


def derivada_centrada(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def newton(f, x0, df=None, tol=1e-10, max_iter=100, h=1e-6):
    x = x0

    for _ in range(max_iter):
        fx = f(x)

        if abs(fx) < tol:
            return x

        dfx = df(x) if df is not None else derivada_centrada(f, x, h)

        if abs(dfx) < 1e-14:
            raise ValueError("Derivada nula o muy pequeña en Newton.")

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return x


