from gpiozero import LED, Button
from time import sleep

def main():
    led_23 = LED(23)
    led_24 = LED(24)
    boton_19 = Button(19, pull_up=True)

    cambio_led23 = 1.0
    contador_23 = 0.0

    led_24_on_tiempo = 1.0
    led_24_off_tiempo = 3.0
    contador_24 = 0.0

    led24_on = False
    boton19_anterior = False

    led_23.off()
    led_24.off()

    tiempo = 0.01

    while True:
        pulsado19 = boton_19.is_pressed

        if pulsado19 and not boton19_anterior:
            contador_23 = 0.0
            contador_24 = 0.0
            led24_on = False
            led_23.off()
            led_24.off()

        boton19_anterior = pulsado19

        contador_23 += tiempo
        contador_24 += tiempo

        if contador_23 >= cambio_led23:
            led_23.toggle()
            contador_23 -= cambio_led23

        if led24_on:
            if contador_24 >= led_24_on_tiempo:
                led_24.off()
                led24_on = False
                contador_24 -= led_24_on_tiempo
        else:
            if contador_24 >= led_24_off_tiempo:
                led_24.on()
                led24_on = True
                contador_24 -= led_24_off_tiempo

        sleep(tiempo)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass