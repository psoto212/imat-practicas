from gpiozero import LED
from time import sleep



def main():
    leds = [20,21,22,23,24,25,26,27]

    led = [LED(p) for p in leds]
    tiempo = 1
    while True:
        for j in led:
            j.on()
            sleep(tiempo)
            j.off()

        if tiempo > 0.001:
            tiempo = max(tiempo/2, 0.001)
        



if __name__ == "__main__":
    try:
        main ()
    except KeyboardInterrupt:
        pass
