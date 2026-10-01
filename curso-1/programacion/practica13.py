class Ordenador:
    def __init__(self, marca, modelo, ram, hd):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.hd = hd
    def __str__(self):
        return f"el ordenador es de la marca {self.marca}, modelo {self.modelo}, con {self.ram}GB de ram y {self.hd} de memoria hd"
    
class Tienda:
  class MarcaNormalizador:
    def __init__(self):
        self.ordenador = {}

    def normalizar_marcas(self, marca_entrada: str) -> str:
        marcas = ["dell", "hp", "lenovo"]

        contador_entrada = {}
        for letra in marca_entrada.lower():
            if letra in contador_entrada:
                contador_entrada[letra] += 1
            else:
                contador_entrada[letra] = 1

        mejor_marca = None
        mejor_puntuacion = -1

        for marca in marcas:
            puntuacion = 0
            for letra in marca:
                if letra in contador_entrada:
                    puntuacion += contador_entrada[letra]

            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_marca = marca

        return mejor_marca


    def normalizar_cpu(cpu_entrada:str):
        cpu = ["i3", "i5", "i7", "i9"]
        cpu_entrada = {}
        for caracter in cpu_entrada:
            if caracter in cpu_entrada:
                cpu_entrada[caracter] += 1
            else:
                cpu_entrada[caracter] = 1

        mejor_cpu = None
        caracteres_correctos = -1

        for cpus in cpu:
            puntuacion = 0
            for caracter in cpu:
                if caracter in cpu_entrada:
                    puntuacion += cpu_entrada[caracter]
            
            if puntuacion > caracteres_correctos:
                caracteres_correctos = puntuacion
                mejor_cpu = cpu
        return mejor_cpu
    

    def normalizar_hd(hd_entrada:str):
        hd = {}
        try:
            for i in hd_entrada:
                if int(i) and int(i+1) and int(i+2):
                    hd[i] = int(i), int(i+1), int(i+2)
                    hd = hd.strip().split(',')
            return hd
        except ValueError as e:
            print(e)
            