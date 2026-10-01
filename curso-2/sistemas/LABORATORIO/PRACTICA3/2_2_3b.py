from gpiozero import LED, Button
from time import sleep

def main() -> None:
    pines_pares = (20, 22, 24, 26)
    pines_impares = (21, 23, 25, 27)

    leds_pares = [LED(pin) for pin in pines_pares]
    leds_impares = [LED(pin) for pin in pines_impares]

    pulsador19 = Button(19, pull_up=True)
    pulsador14 = Button(14, pull_up=True, bounce_time=0.05)

    # Estado mutable para poder cambiarlo dentro del callback
    estado = {"impares_on": False}

    def toggle_impares(leds, st) -> None:
        st["impares_on"] = not st["impares_on"]
        for led in leds:
            led.on() if st["impares_on"] else led.off()

    # Callback usando lambda para "capturar" leds_impares y estado
    pulsador14.when_pressed = lambda: toggle_impares(leds_impares, estado)

    while True:
        # Pares: solo mientras se presiona GPIO19 (por nivel)
        if pulsador19.is_pressed:
            for led in leds_pares:
                led.on()
        else:
            for led in leds_pares:
                led.off()

        sleep(0.01)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")