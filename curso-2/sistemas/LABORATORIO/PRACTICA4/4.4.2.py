from gpiozero import PWMLED, Button
from threading import Timer,Event

def main():
    pines_A = (20,21,22,23)
    leds_A = [PWMLED(pin, frequency=100) for pin in pines_A]


    pines_B = (24, 25, 26, 27)
    leds_B = [PWMLED(pin, frequency=100) for pin in pines_B]

    estado = {"nivel_A": 0.0, "nivel_B": 0.0,"timer_A":None, "timer_B":None}
    for led in leds_A + leds_B:
        led.value = 0.0
    
    def actualizar_brillo_A():
        estado["nivel_A"] += 0.2

        if estado["nivel_A"] > 1.0:
            estado["nivel_A"] = 0.0
        
        for led in leds_A:
            led.value = estado["nivel_A"]
        
        estado["timer_A"] = Timer(1.0, actualizar_brillo_A)
        estado["timer_A"].start()

    def actualizar_brillo_B():
        estado["nivel_B"] += 0.2

        if estado["nivel_B"] > 1.0:
            estado["nivel_B"] = 0.0
        
        for led in leds_B:
            led.value = estado["nivel_B"]
        
        estado["timer_B"] = Timer(0.5, actualizar_brillo_B)
        estado["timer_B"].start()
    
    try:
        actualizar_brillo_A()
        actualizar_brillo_B()
        Event().wait()
    finally:
        if estado["timer_A"] is not None:
            estado["timer_A"].cancel()
        if estado["timer_B"] is not None:
            estado["timer_B"].cancel()
        for led in leds_A + leds_B:
            led.off()
            led.close()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")
