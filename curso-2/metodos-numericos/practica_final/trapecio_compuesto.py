import numpy as np

def trapecio(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n

    S = h/2*(y[0] + y[-1]) + h*np.sum(y[1:-1])

    return S





#y[1:-1], es desde el segundo hasta el penultimo
