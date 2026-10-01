[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iCn72rXQ)
# Práctica 2 - Roomba

En esta práctica implementaremos un agente inteligente que controle una Roomba (robot aspirador) en distintos entornos 2D. El objetivo del agente es limpiar las celdas sucias del entorno de manera eficiente, intentando minimizar el número de movimientos realizados. En este caso tenemos tres tipos de entorno:
- **Entorno 1**: Un entorno simple con 2 celdas sucias, una al lado de la otra.
- **Entorno 2**: Un entorno con $n$ celdas sucias en fila, donde $n$ es un parámetro que podemos variar.
- **Entorno 3**: Un entorno rectangular con $n \times m$ celdas sucias, donde $n$ y $m$ son parámetros que podemos variar.

Para los detalles completos de la práctica recuerda consultar el enunciado del pdf y la plantilla de código disponible en Moodle.

## Uso del repositorio

Clona el repositorio de la práctica en tu máquina local:

```bash
git clone <url de tu repositorio> 
```

Una vez clonado, navega al directorio del proyecto para poder trabajar en él.

```bash
cd roomba_lab_final
```

Asegúrate de tener las dependencias necesarias instaladas (comprueba el archivo `requirements.txt`). Conviene crear un entorno virtual para gestionar las dependencias (opcional pero recomendado).

```bash
python -m venv venv
source venv/bin/activate     # En Linux/Mac
venv\Scripts\activate        # En Windows
```

Si has decidido usar un entorno virtual, instala las dependencias dentro de él:

```bash
pip install -r requirements.txt
```
## La tarea

Tu tarea consistirá en rellenar las partes marcadas con `"YOUR CODE GOES HERE"` en el archivo `src/agents.py`, que es el fichero encargado de la implementación de los agentes buscadores que controlan la Roomba para cada escenario. 

## Usar los tests

Antes de hacer el envío de la entrega, asegúrate de que todo funciona correctamente ejecutando los tests incluidos en el repositorio. Puedes hacerlo con el siguiente comando:

```bash
pytest tests/test_agents.py
```

## Envío de la entrega
Para enviar tu solución, simplemente sube los cambios a tu repositorio de GitHub. Asegúrate de que todos los tests pasen correctamente antes de hacer el envío. 

Guarda tu progreso añadiendo los archivos modificados y haciendo un commit (puedes cambiar el mensaje en el commit por uno que describa mejor tus cambios):
```bash
git add .
git commit -m "Implementación inicial del agente Roomba"
```

Para subir tu trabajo al repositorio remoto en GitHub y pasar los tests automáticos, haz lo siguiente:
```bash
git push origin main
```
Cada vez que hagas `push`, GitHub Classroom lanzará la corrección automática de tu código. Asegúrate de que todos los tests pasen correctamente antes de la fecha límite de entrega.