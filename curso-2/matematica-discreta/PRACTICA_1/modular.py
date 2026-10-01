"""
modular.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas
"""

from typing import Tuple, List, Dict
from math import isqrt

class IncompatibleEquationError(Exception):
    pass

def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def lista_primos(a: int, b: int) -> List[int]:
    return [i for i in range(a, b) if es_primo(i)]

def factorizar(n: int) -> Dict[int, int]:
    if n in (0, 1, -1):
        return {}
    factores: Dict[int, int] = {}
    num = abs(n)
    while num % 2 == 0:
        factores[2] = factores.get(2, 0) + 1
        num //= 2
    d = 3
    while d * d <= num:
        while num % d == 0:
            factores[d] = factores.get(d, 0) + 1
            num //= d
        d += 2
    if num > 1:
        factores[num] = factores.get(num, 0) + 1
    return factores

def mcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def bezout(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    d, x1, y1 = bezout(b, a % b)
    return (d, y1, x1 - (a // b) * y1)

def mcd_n(nlist: List[int]) -> int:
    if not nlist:
        raise ValueError("Lista vacía")
    res = abs(nlist[0])
    for n in nlist[1:]:
        res = mcd(res, n)
    return res

def bezout_n(nlist: List[int]) -> Tuple[int, List[int]]:
    if not nlist:
        raise ValueError("Lista vacía")
    d, x, y = bezout(nlist[0], nlist[1])
    coefs = [x, y] + [0] * (len(nlist) - 2)
    for i in range(2, len(nlist)):
        d2, u, v = bezout(d, nlist[i])
        coefs = [c * u for c in coefs] + [0]
        coefs[i] = v
        d = d2
    return d, coefs

def coprimos(a: int, b: int) -> bool:
    return mcd(a, b) == 1

def potencia_mod_p(base: int, exp: int, p: int) -> int:
    if p == 0:
        raise IncompatibleEquationError("El módulo no puede ser 0")
    return pow(base, exp, p)

def inversa_mod_p(n: int, p: int) -> int:
    if p == 0:
        raise IncompatibleEquationError("El módulo no puede ser 0")
    if mcd(n, p) != 1:
        raise IncompatibleEquationError("No existe inversa modular")
    return pow(n, -1, p)

def euler(n: int) -> int:
    res = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            res -= res // p
        p += 1
    if n > 1:
        res -= res // n
    return res

def legendre(n: int, p: int) -> int:
    if p == 0:
        raise IncompatibleEquationError("El módulo no puede ser 0")
    n %= p
    if n == 0:
        return 0
    r = pow(n, (p - 1) // 2, p)
    return -1 if r == p - 1 else r

def resolver_sistema_congruencias(alist: List[int], blist: List[int], plist: List[int]) -> Tuple[int, int]:
    if len(alist) != len(blist) or len(alist) != len(plist):
        raise ValueError("Listas de distinta longitud")
    M = 1
    for p in plist:
        M *= p
    x = 0
    for a, b, p in zip(alist, blist, plist):
        M_i = M // p
        inv = inversa_mod_p(M_i, p)
        x += a * b * inv * M_i
    return x % M, M

# Opcionales
def raiz_mod_p(n: int, p: int) -> int:
    raise IncompatibleEquationError("Opcional no implementado")

def ecuacion_cuadratica(a: int, b: int, c: int, p: int) -> Tuple[int, int]:
    raise IncompatibleEquationError("Opcional no implementado")
