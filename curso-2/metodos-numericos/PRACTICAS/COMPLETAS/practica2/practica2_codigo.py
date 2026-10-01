import numpy as np
import matplotlib.pyplot as plt

# EJERCICIO 4

def diferencia_dividida(x:list, y:list) -> list:
    """
    Calcula la tabla de diferencias divididas.
    Args:
        - x(list(int)): valores en el eje x de los puntos
        - y(list(int)): imagenes de los valores x en la funcion
    Return:
        - dd(list(int)): lista con las diferencias divididas de cada orden
    """
    n = len(x)
    dd = y.copy()

    for k in range(1, n):
        for i in range(n-1, k-1, -1):
            dd[i] = (dd[i] - dd[i-1]) / (x[i] - x[i-k])

    return dd


def polinomio_interpolador_newton(x:list, y:list, t:float) -> float:
    """
    Calcula la aproximación de un valor t.
    Args:
        - x(list(int)): valores en el eje x de los puntos
        - y(list(int)): imagenes de los valores x en la funcion
        - t(float): valor a aproximar
    Return:
        - p(float): aproximación del valor t en el polinomio interpolador
    """
    # t tiene que estar entre los valores de x
    if t<x[0] or t>x[-1]:
        raise ValueError("El punto a aproximar debe estar en un rango entre los valores de x")

    a = diferencia_dividida(x, y)

    p = a[-1]
    
    for i in range(len(a)-2, -1, -1):
        p = a[i] + (t-x[i]) * p

    return p


# EJERCICIO 5

def evaluar_en_lista(x, y, t_list):
    return [polinomio_interpolador_newton(x, y, t) for t in t_list]

def grafica_polinomio_interpolador(f, x_nodes, y_nodes, a, b, m=1000):
    x_grid = np.linspace(a, b, m).tolist()
    y_f = f(np.array(x_grid))
    y_p = np.array(evaluar_en_lista(x_nodes, y_nodes, x_grid))

    plt.figure()
    plt.plot(x_grid, y_f)
    plt.plot(x_grid, y_p)
    plt.scatter(x_nodes, y_nodes)
    plt.grid(True)
    plt.legend(["f(x)", "P_n(x)", "nodos"])
    plt.show()

# EJERCICIO 6

def f_6(x):
    return 1/(1+x**2)

def f_7(x):
    return (np.sin(x))

def ejercicio_6():
    a, b = -5, 5
    x_grid = np.linspace(a, b, 2000).tolist()

    for n in [4, 8, 12, 16]:
        x_nodes = np.linspace(a, b, n+1).tolist()
        y_nodes = f_6(np.array(x_nodes)).tolist()

        y_p = np.array(evaluar_en_lista(x_nodes, y_nodes, x_grid))
        y_f = f_6(np.array(x_grid))

        err = np.max(np.abs(y_f - y_p))
        print(f"\t· Grado {n}: error máximo aprox = {err:.3e}")

        plt.figure()
        plt.plot(x_grid, y_f)
        plt.plot(x_grid, y_p)
        plt.scatter(x_nodes, y_nodes)
        plt.title(f"f(x)=1/(1+x^2), grado {n}, equiespaciados")
        plt.legend(["f(x)", "P_n(x)", "nodos"])
        plt.grid(True)
        plt.show()

# EJERCICIO 8

def ejercicio_8():
    a, b = -1, 1
    x_grid = np.linspace(a, b, 2000).tolist()

    for n in [5, 10, 15, 20]:
        x_nodes = [-1 + 2*k/n for k in range(n+1)]
        y_nodes = [abs(xi) for xi in x_nodes]

        y_p = np.array(evaluar_en_lista(x_nodes, y_nodes, x_grid))
        y_f = np.abs(np.array(x_grid))

        plt.figure()
        plt.plot(x_grid, y_f)
        plt.plot(x_grid, y_p)
        plt.scatter(x_nodes, y_nodes)
        plt.title(f"f(x)=|x|, n={n}")
        plt.legend(["f(x)", "P_n(x)", "nodos"])
        plt.grid(True)
        plt.show()


if __name__ == "__main__":

    print("Test")
    x = [1,2,3]
    y = [0,3,8]
    t = 1.75
    print(f"Calcular la aproximación de {t} dados los puntos x = {x}, y = {y}")
    print(f"f[{t}] = {polinomio_interpolador_newton(x, y, t)}")

    # EJERCICIO 6
    print("\nPolinomio interpolador de la funcion 1/(1+x2) en [-5,5]")
    ejercicio_6()
    """
    Según la formula del error, con nodos equidistantes el producto toma valores muy grandes cerca 
    de +-5, por lo que el error se amplifica en los extremos.
    """
    # EJERCICIO 7
    """
    Si probamos el ejercicio 6 con la funcion f = sin(x) (cambiar código ej6), podemos observar como 
    el error va disminuyendo considerablemente a medida que aumentamos el grado del polinomio, es decir,
    el número de puntos que interpolamos.
    """

    # EJERCICIO 8
    ejercicio_8()
    """
    Pn interpola los puntos pero cerca de 0 suele fallar mas, porque |x| tiene una punta en  0 
    y los polinomios no la pueden imitar bien. Por lo tanto, la interpolacion converge de manera
    más lenta y el mayor error está alrededor de 0.
    """