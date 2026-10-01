from datetime import datetime

class Registro:
    def __init__(self, archivo="registros_partidas.txt"):
        self.archivo = archivo

    def guardar_registro(self, jugador1, jugador2, ganador):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        registro = f"Partida: {jugador1.nombre} vs {jugador2.nombre}, Ganador: {ganador}, Fecha: {fecha_hora}\n"
        
        with open(self.archivo, 'a') as file:
            file.write(registro)
        
        print(f"Registro guardado en {self.archivo}: {jugador1.nombre} vs {jugador2.nombre}, ganador: {ganador} en {fecha_hora}")
