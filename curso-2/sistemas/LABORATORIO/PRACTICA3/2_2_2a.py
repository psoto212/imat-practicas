from gpiozero import LED, Button
from time import sleep

def main() -> None:
    pines_pares = (20, 22, 24, 26)
    leds_pares = [LED(pin) for pin in pines_pares]

    pulsador19 = Button(19, pull_up=True)  # pull-up (pulsado => is_pressed True)

    while True:
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


    