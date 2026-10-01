from gpiozero import LEDBoard, Button
from time import sleep

def main() -> None:
    leds_pares = LEDBoard(20, 22, 24, 26)
    pulsador19 = Button(19, pull_up=True)

    while True:
        if pulsador19.is_pressed:
            leds_pares.on()
        else:
            leds_pares.off()

        sleep(0.01)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")