from gpiozero import LED, Button
from time import sleep


"""
enunciado
Ejercicio 1: escribe un programa con gpiozero en el que los LED pares GPIO20, GPIO22, GPIO24 y GPIO26 
estén encendidos normalmente, pero se apaguen mientras se mantenga pulsado GPIO19. Además, 
cada pulsación en GPIO17 debe invertir el estado de todos los LED impares. 
Aquí mezclas control por nivel para un botón y por flanco para otro, que es justo una de las ideas centrales de la práctica

"""

def main():
    pines_pares = (20, 22, 24, 26)
    pines_impares = (21, 23, 25, 27)

    leds_pares = [LED(pin) for pin in pines_pares]
    leds_impares = [LED(pin) for pin in pines_impares]

    boton_pares = Button(19, pull_up=True)
    boton_impares = Button(17, pull_up=True)

    estado = {"impares_on": False}

    def mostrar_impares():
        for led in leds_impares:
            if estado["impares_on"]:
                led.on()
            else:
                led.off()

    def toggle_impares():
        estado["impares_on"] = not estado["impares_on"]
        mostrar_impares()

    boton_impares.when_pressed = toggle_impares

    mostrar_impares()

    while True:
        if boton_pares.is_pressed:
            for led in leds_pares:
                led.off()
        else:
            for led in leds_pares:
                led.on()
        sleep(0.05)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")