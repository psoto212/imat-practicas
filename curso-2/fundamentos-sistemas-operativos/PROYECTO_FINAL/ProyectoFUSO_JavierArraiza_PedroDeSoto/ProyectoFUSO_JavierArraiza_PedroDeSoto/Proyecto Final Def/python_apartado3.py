import sys
import os

def main():
	if len(sys.argv) != 1:
		sys.exit(1)
	
	carpeta = "filtered"
	if not os.path.isdir(carpeta):
		sys.exit(1)
	
	for nombre_fichero in os.listdir(carpeta):
		ruta_fichero = os.path.join(carpeta, nombre_fichero)
		
		if not os.path.isfile(ruta_fichero):
			continue

		procesar_fichero(ruta_fichero)

def procesar_fichero(ruta_fichero):

	usuarios = set()
	localizaciones = set()
	filas_completas = 0
	checks_in_2010_07 = 0
	checks_in_2010_08 = 0

	with open(ruta_fichero, "r", encoding="utf-8") as fichero:
		for linea in fichero:
			linea = linea.rstrip("\n")
			if len(linea) == 0:
				continue

			partes = linea.split()
			
			if len(partes) < 3:
				continue

			usuario = partes[0]
			fecha = partes[1]
			localizacion = partes[2]
		
			filas_completas += 1
			usuarios.add(usuario)
			localizaciones.add(localizacion)

			if "2010-07" in fecha:
				checks_in_2010_07 += 1
			elif "2010-08" in fecha:
				checks_in_2010_08 += 1

	nombre = os.path.basename(ruta_fichero)
	nombre_ciudad = nombre.replace("filtered.txt","")
	
	print(f"""Estadisticas para {nombre_ciudad}
Numero de usuarios distintos: {len(usuarios)}
Numero de localizaciones distintas: {len(localizaciones)}
Numero de filas completas: {filas_completas}
Numero de checks-in 2010_07: {checks_in_2010_07}
Numero de checks-in 2010_08: {checks_in_2010_08}
""")

if __name__ == "__main__":
	main()
