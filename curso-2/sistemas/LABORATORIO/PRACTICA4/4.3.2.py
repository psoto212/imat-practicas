from gpiozero import LED, Button
from time import sleep

def main() -> None:
    boton_7 = Button(7, pull_up=True)
    led_23 = LED(23)
    led_24 = LED(24)

    cambio_par = 0.5
    cambio_impar = 2.5
    cambio_led23 = cambio_par
    contador23 = 0.0

    led_24_on = 1.25
    led_24_off = 3.75
    contador24 = 0.0
    led24_on = False


    pulsaciones = 0
    btn_ant = boton_7.is_pressed

    led_23.on()
    led_24.on()
    led24_on = True

    tiempo = 0.01

    while True:
        btn_act = boton_7.is_pressed
        if (btn_ant is False) and (btn_act is True):
            pulsaciones += 1

            cambio_led23 = cambio_impar if (pulsaciones % 2 == 1) else cambio_par

            led_23.on()
            led_24.on()
            led24_on = True
            contador23 = 0.0
            contador24 = 0.0

        btn_ant = btn_act

        contador23 += tiempo
        contador24 += tiempo

        if contador23 >= cambio_led23:
            led_23.toggle()
            contador23 -= cambio_led23

        if led24_on:
            if contador24 >= led_24_on:
                led_24.off()
                led24_on = False
                contador24 -= led_24_on
        else:
            if contador24 >= led_24_off:
                led_24.on()
                led24_on = True
                contador24 -= led_24_off

        sleep(tiempo)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")
