from gpiozero import LEDBoard, Button
from time import sleep, time

"""
Haz un programa con `gpiozero` para 8 LED `GPIO20–GPIO27` y 3 botones `GPIO19`, `GPIO17` y `GPIO16`. Debe haber un `contador` módulo 256
y dos modos: **binario** y **barra**. Al empezar, el modo es binario y el contador vale 0. 
En modo binario, los LED muestran el contador en binario. 
En modo barra, muestran cuántos grupos de 32 tiene el contador, de 0 a 8 LED encendidos.
`GPIO19` suma 1 por pulsación y `GPIO17` resta 1 por pulsación, ambos **por flanco**. `GPIO16` tiene doble función: 
pulsación corta cambia de modo y pulsación larga de más de 2 segundos pone el contador a 0 sin cambiar de modo. 
Cada vez que cambie algo, hay que actualizar los LED al momento.
Además, si el contador llega exactamente a `0` o a `255`, antes de mostrar el resultado final todos los LED deben parpadear dos veces. 
El programa tiene que estar organizado en funciones, no meter toda la lógica dentro del `while True`.
"""




def main():
    leds = LEDBoard(20, 21, 22, 23, 24, 25, 26, 27)

    boton_suma = Button(19, pull_up=True)
    boton_resta = Button(17, pull_up=True)
    boton_modo = Button(16, pull_up=True)

    estado = {
        "contador": 0,
        "modo": "binario",      # "binario" o "barra"
        "t_inicio_modo": 0
    }

    def parpadear_limite():
        for _ in range(2):
            leds.on()
            sleep(0.2)
            leds.off()
            sleep(0.2)

    def actualizar_leds():
        contador = estado["contador"]

        if estado["modo"] == "binario":
            bits = [(contador >> bit) & 1 for bit in range(8)]
            leds.value = bits
        else:
            bloques = contador // 32
            valores = [1 if i < bloques else 0 for i in range(8)]
            leds.value = valores

    def comprobar_limite():
        if estado["contador"] == 0 or estado["contador"] == 255:
            parpadear_limite()
        actualizar_leds()

    def sumar():
        estado["contador"] = (estado["contador"] + 1) & 0xFF
        comprobar_limite()

    def restar():
        estado["contador"] = (estado["contador"] - 1) & 0xFF
        comprobar_limite()

    def inicio_pulsacion_modo():
        estado["t_inicio_modo"] = time()

    def fin_pulsacion_modo():
        duracion = time() - estado["t_inicio_modo"]

        if duracion >= 2:
            estado["contador"] = 0
        else:
            if estado["modo"] == "binario":
                estado["modo"] = "barra"
            else:
                estado["modo"] = "binario"

        comprobar_limite()

    boton_suma.when_pressed = sumar
    boton_resta.when_pressed = restar
    boton_modo.when_pressed = inicio_pulsacion_modo
    boton_modo.when_released = fin_pulsacion_modo

    actualizar_leds()

    while True:
        sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")