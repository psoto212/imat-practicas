def elevar(numero, potencia):
    if (type(numero) == int or type(numero) == float) and (type(potencia) == int or type(potencia) == float):
        numero_nuevo = numero ** potencia
    return numero_nuevo

def raiz_cuadrada(numero):
    if type(numero) == int or type(numero) == float:
        numero_nuevo = numero.sqrt()
    return numero_nuevo


def raiz_cubica(numero):
    if type(numero) == int or type(numero) == float:
        numero_nuevo = numero.sqrt(3)
    return numero_nuevo
    