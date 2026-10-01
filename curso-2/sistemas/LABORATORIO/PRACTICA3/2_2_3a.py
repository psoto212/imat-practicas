from gpiozero import LED, Button
from time import sleep

def main() -> None:
    pines_pares = (20, 22, 24, 26)
    pines_impares = (21, 23, 25, 27)

    leds_pares = [LED(pin) for pin in pines_pares]
    leds_impares = [LED(pin) for pin in pines_impares]

    pulsador19 = Button(19, pull_up=True)
    pulsador14 = Button(14, pull_up=True)

    impares_on = False
    puls14_anterior = pulsador14.is_pressed

    while True:
        # Pares: solo mientras se presiona GPIO19
        if pulsador19.is_pressed:
            for led in leds_pares:
                led.on()
        else:
            for led in leds_pares:
                led.off()

        # Impares: toggle con flanco (False -> True) en GPIO14
        puls14_actual = pulsador14.is_pressed
        if (puls14_anterior is False) and (puls14_actual is True):
            impares_on = not impares_on
            for led in leds_impares:
                led.on() if impares_on else led.off()

        puls14_anterior = puls14_actual
        sleep(0.01)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")