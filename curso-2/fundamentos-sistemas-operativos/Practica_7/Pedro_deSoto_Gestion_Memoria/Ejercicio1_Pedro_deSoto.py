import numpy as np
import sys

tipos = [np.bool_, np.int8, np.int16, np.int32, np.int64,
         np.float16, np.float32, np.float64, np.complex64, np.complex128]

print("== Parte 1 ==")
for t in tipos:
    arr = np.array([0], dtype=t)
    print(t.__name__, "->", arr.itemsize, "bytes")

print("\n== Parte 2 ==")
u1 = np.array(["a"], dtype="U1")
u5 = np.array(["abcde"], dtype="U5")
s1 = np.array([b"a"], dtype="S1")
s5 = np.array([b"abcde"], dtype="S5")

print("U1:", u1.nbytes, "bytes")
print("U5:", u5.nbytes, "bytes")
print("S1:", s1.nbytes, "bytes")
print("S5:", s5.nbytes, "bytes")

print("\n== Parte 3 ==")
print("Entero Python (1):", sys.getsizeof(1), "bytes")
print("Float Python (1.0):", sys.getsizeof(1.0), "bytes")
print("String 1 char:", sys.getsizeof("a"), "bytes")
print(f"String 5 chars:", sys.getsizeof("abcde"), "bytes")
