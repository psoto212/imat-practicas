from gpiozero import PWMLED, Button
from threading import Timer,Event

def main():
    pines = (20,21,22,23,24,25,26,27)
    leds = [PWMLED(pin, frequency=100) for pin in pines]
    estado = {"nivel": 0.0, "timer":None}

    for led in leds:
        led.value = 0.0
    
    def actualizar_brillo():
        estado["nivel"] += 0.2

        if estado["nivel"] > 1.0:
            estado["nivel"] = 0
        
        for led in leds:
            led.value = estado["nivel"]
        
        estado["timer"] = Timer(1.0, actualizar_brillo)
        estado["timer"].start()
    
    try:
        actualizar_brillo()
        Event().wait()
    finally:
        if estado["timer"] is not None:
            estado["timer"].cancel()
        for led in leds:
            led.off()
            led.close()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")
