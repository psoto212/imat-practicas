import RPi.GPIO as GPIO
import time

def main() -> None:
    GPIO.setmode(GPIO.BCM)
    leds_pares = (20,22,24,26)
    leds_impares = (21,23,25,27)
    pulsador19 = 19
    pulsador14 = 14

    GPIO.setup(leds_pares, GPIO.OUT, initial = GPIO.LOW) #configurar las salidas
    GPIO.setup(leds_impares, GPIO.OUT, initial = GPIO.LOW) 
    GPIO.setup((pulsador19, pulsador14),GPIO.IN, pull_up_down=GPIO.PUD_UP)

    impares = False
    puls14_ant = GPIO.input(pulsador14)

    while True:
        if GPIO.input(pulsador19) == GPIO.LOW:
            GPIO.output(leds_pares, GPIO.HIGH) #encender los pares
        else:
            GPIO.output(leds_pares, GPIO.LOW) #apagar los pares

        puls14_act = GPIO.input(pulsador14)

        if (puls14_ant == GPIO.HIGH) and (puls14_act == GPIO.LOW):
            impares = not impares
            GPIO.output(leds_impares, GPIO.HIGH if impares else GPIO.LOW)
        
        puls14_ant = puls14_act

        time.sleep(0.01)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()