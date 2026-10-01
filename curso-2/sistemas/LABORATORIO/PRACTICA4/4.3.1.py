from gpiozero import LED, Button
from time import sleep


def main():
    led_23 = LED(23)
    led_24 = LED(24)


    cambio_led23 = 0.5
    contador_23 = 0.0


    led_24_on = 1.25
    led_24_off = 3.75
    contador_24 = 0.0

    led24_on = False

    led_23.off()
    led_24.off()

    tiempo = 0.01

    while True:
        contador_23 += tiempo
        contador_24 += tiempo

        if contador_23 >=   cambio_led23:
            led_23.toggle()
            contador_23 -=  cambio_led23
        


        if led24_on:
            if contador_24 >= led_24_on:
                led_24.off()
                led24_on = False
                contador_24 -= led_24_on


        else:
            if contador_24 >= led_24_off:
                led_24.on()
                led24_on = True
                contador_24 -= led_24_off

        sleep(tiempo)




if __name__ == "__main__":
    try:
        main ()
    except KeyboardInterrupt:
        pass
 