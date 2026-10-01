from gpiozero import LED, Button
from time import sleep

def main():
    led_23 = LED(23)
    led_24 = LED(24)

    boton_19 = Button(19, pull_up=True)
    boton_17 = Button(17, pull_up=True)

    medio_periodo_23 = 1.0
    contador_23 = 0.0

    tiempo_on_24 = 1.0
    tiempo_off_24 = 2.0
    contador_24 = 0.0
    led24_on = False

    boton19_anterior = False
    boton17_anterior = False

    tiempo = 0.01

    led_23.off()
    led_24.off()

    while True:
        pulsado19 = boton_19.is_pressed
        pulsado17 = boton_17.is_pressed

        if pulsado19 and not boton19_anterior:
            if medio_periodo_23 == 1.0:
                medio_periodo_23 = 0.5
            else:
                medio_periodo_23 = 1.0

        if pulsado17 and not boton17_anterior:
            contador_23 = 0.0
            contador_24 = 0.0
            led24_on = False
            led_23.off()
            led_24.off()

        boton19_anterior = pulsado19
        boton17_anterior = pulsado17

        contador_23 += tiempo
        contador_24 += tiempo

        if contador_23 >= medio_periodo_23:
            led_23.toggle()
            contador_23 -= medio_periodo_23

        if led24_on:
            if contador_24 >= tiempo_on_24:
                led_24.off()
                led24_on = False
                contador_24 -= tiempo_on_24
        else:
            if contador_24 >= tiempo_off_24:
                led_24.on()
                led24_on = True
                contador_24 -= tiempo_off_24

        sleep(tiempo)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass