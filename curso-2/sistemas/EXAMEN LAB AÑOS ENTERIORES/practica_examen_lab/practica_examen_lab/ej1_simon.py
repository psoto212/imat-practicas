import random
from gpiozero import Button, LED
from signal import pause
import time

def main():
    # Definición de LEDs
    leds_referencia = [LED(23), LED(21), LED(22)]
    led_pins2 = [26, 27, 25]
    leds_contadores = [LED(pin) for pin in led_pins2]

    # Definición de botones
    button19 = Button(19)
    button17 = Button(17)
    button16 = Button(16)
    button7 = Button(7)

    # Variables de control
    contador = 1
    respuesta = []
    cadena_numerica = []
    error = False
    indice_mostrar = 0
    mostrando_secuencia = True

    # Función para actualizar los LEDs del contador
    def actualizar_leds():     
        bits = [(contador >> bit) & 0x1 for bit in range(3)] 
        for i, estado in enumerate(bits):  
            leds_contadores[i].value = estado  

    # Función para avanzar en la secuencia de visualización
    def avanzar():
        global indice_mostrar, mostrando_secuencia
        if indice_mostrar < len(cadena_numerica):
            numero = cadena_numerica[indice_mostrar]
            for led in leds_referencia:
                led.off()
            leds_referencia[numero].on()
            indice_mostrar += 1
        else:
            mostrando_secuencia = False
            for led in leds_referencia:
                led.off()

    # Función para manejar la entrada del usuario
    def botones(presionado):
        global respuesta, cadena_numerica, error
        if mostrando_secuencia:
            return  
        respuesta.append(presionado)
        if respuesta == cadena_numerica[:len(respuesta)]:
            if len(respuesta) == len(cadena_numerica):
                error = False
                generar_cadenas()
        else:
            error = True
            generar_cadenas()
        
    # Función para generar la secuencia aleatoria
    def generar_cadenas():
        global contador, error, cadena_numerica, respuesta, indice_mostrar, mostrando_secuencia
        if error:
            contador = 1
            error = False
        else:
            contador += 1

        cadena_numerica = []
        ultimo = -1
        for _ in range(contador):
            numero = random.randint(0, 2)
            while numero == ultimo:
                numero = random.randint(0, 2)
            ultimo = numero
            cadena_numerica.append(numero)

        respuesta = []
        indice_mostrar = 0
        mostrando_secuencia = True
        actualizar_leds()
        avanzar()
    
    # Iniciar el juego
    actualizar_leds()
    generar_cadenas()

    # Asignar funciones a los botones
    button7.when_pressed = avanzar
    button16.when_pressed = lambda: botones(0)
    button17.when_pressed = lambda: botones(1)
    button19.when_pressed = lambda: botones(2)

    # Mantener el script en ejecución
    pause()

# Ejecutar el programa
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
