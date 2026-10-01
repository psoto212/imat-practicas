from gpiozero import Button, LED, LEDBoard, PWMLED, MCP3008
from signal import pause
import time

# ej1
def main():
    puls = Button(19)
    leds = [LED(20), LED(21), LED(22), LED(23), LED(24), LED(25), 
            LED(26), LED(27)] 
    fibonachi = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    j = 0

    def actualizar_leds(contador): 
        bits = [(contador >> bit) & 0x1 for bit in range(8)] 
        for i, bit in enumerate(bits): 
            if bit == 1: 
                leds[i].on() 
            else: 
                leds[i].off() 
                
    def incrementar():
        nonlocal j
        j += 1
        if j >= len(fibonachi):
            j = 0
        actualizar_leds(fibonachi[j])

    actualizar_leds(fibonachi[j])
    puls.when_pressed = incrementar
    pause()

# ej2 COMPROBAR EN EL OSCILOSCOPIO!!!!! 
def main2():
    puls = Button(19)
    leds = [LED(20), LED(21), LED(22), LED(23), LED(24), LED(25), 
            LED(26), LED(27)] 
    fibonachi = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    j = 0

    def actualizar_leds(contador): 
        bits = [(contador >> bit) & 0x1 for bit in range(8)]
        for led in leds:
            led.off() 
        if contador < 30:
            for i, bit in enumerate(bits): 
                if bit == 1: 
                    leds[i].blink(0.1,0.1) # si uso .pulse(0.1,0.1) no es necesario apagar
                                            # todos los leds de primeras.
                else: 
                    leds[i].off() 
        else:
            for i, bit in enumerate(bits): 
                if bit == 1: 
                    leds[i].blink(0.5,0.5)
                else: 
                    leds[i].off() 

    def incrementar():
        nonlocal j
        j += 1
        if j >= len(fibonachi):
            j = 0
        actualizar_leds(fibonachi[j])

    actualizar_leds(fibonachi[j])
    puls.when_pressed = incrementar
    pause()

# ej3
def main3():
    sensor = MCP3008(channel=7) 
    puls = Button(19)
    leds = [LED(20), LED(21), LED(22), LED(23), LED(24), LED(25), 
            LED(26), LED(27)] 
    fibonachi = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    j = 0

    def actualizar_leds(contador): 
        bits = [(contador >> bit) & 0x1 for bit in range(8)]
        for led in leds:
            led.off() 
        if contador < 30:
            for i, bit in enumerate(bits): 
                if bit == 1: 
                    leds[i].blink(0.1,0.1) # si uso .pulse(0.1,0.1) no es necesario apagar
                                            # todos los leds de primeras.
                else: 
                    leds[i].off() 
        else:
            for i, bit in enumerate(bits): 
                if bit == 1: 
                    leds[i].blink(0.5,0.5)
                else: 
                    leds[i].off() 

    def incrementar():
        nonlocal j
        j += 1
        if j >= len(fibonachi):
            j = 0
        actualizar_leds(fibonachi[j])
    def decrementar():
        nonlocal j
        j -= 1
        if j <0:
            j = 0
        actualizar_leds(fibonachi[j])
    
    actualizar_leds(fibonachi[j])
    puls.when_pressed = incrementar

    while True:
        voltios = sensor.voltage
        if voltios < 1:
            decrementar()
            time.sleep(0.5)
            
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
         pass        