from gpiozero import Button, LEDBoard
from signal import pause

def main():
    boton = Button(7)
    leds_centrales = LEDBoard(22,23,24,25)
    leds_externos = LEDBoard(20,21,26,27)

    while True:
        if boton.is_pressed:
            leds_externos.off()
            leds_centrales.on()
        else:
            leds_centrales.off()
            leds_externos.on()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass