#biseccion
def biseccion(f, a, b, tol):
    while b-a > tol:
        c = (a+b)/2

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return a, b


#secante
def secante(f, x0, x1, tolx, toly, nmax):
    n = 0
    errx = 10*tolx
    erry = 10*toly

    while (errx > tolx or erry > toly) and n < nmax:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))

        errx = abs(x2-x1)
        erry = abs(f(x2))

        x0 = x1
        x1 = x2
        n = n + 1

    return x2, n, errx, erry



#newton

def newton(f, df, x0, tolx, toly, nmax):
    n = 0
    errx = 10*tolx
    erry = 10*toly

    while (errx > tolx or erry > toly) and n < nmax:
        x1 = x0 - f(x0)/df(x0)

        errx = abs(x1-x0)
        erry = abs(f(x1))

        x0 = x1
        n = n + 1

    return x1, n, errx, erry

#newton sin derivada exacta
def newton_sin_derivada(f, x0, h, tol, nmax):
    n = 0
    error = 10*tol

    while error > tol and n < nmax:
        df = (f(x0+h) - f(x0-h))/(2*h)

        x1 = x0 - f(x0)/df

        error = abs(x1-x0)

        x0 = x1
        n = n + 1

    return x1, n


#punto fijo
def punto_fijo(g, x0, tol, nmax):
    n = 0
    error = 10*tol

    while error > tol and n < nmax:
        x1 = g(x0)

        error = abs(x1 - x0)

        x0 = x1
        n = n + 1

    return x1, n