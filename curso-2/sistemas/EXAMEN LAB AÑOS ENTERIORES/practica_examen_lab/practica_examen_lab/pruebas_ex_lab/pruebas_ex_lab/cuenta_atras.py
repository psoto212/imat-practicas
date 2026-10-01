# ej1
from gpiozero import Button, LED, LEDBoard, PWMLED, MCP3008
from signal import pause
import time
import random

def main():
    puls_7 = Button(7)
    puls_16 = Button(16)
    puls_17 = Button(17)
    puls_19 = Button(19)

    leds_jug = LEDBoard(24,25,26,27)
    leds_jug.off()
    leds_ref = [LED(20), LED(21), LED(22), LED(23)] 

    def jugador(i):
        leds_jug[i].toggle()

    reiniciar = True
    while True:
        if reiniciar:
            num = random.randint(1,15)
            reiniciar = False

        bits = [(num >> bit) & 0x1 for bit in range(4)] 
        for i, bit in enumerate(bits): 
            if bit == 1: 
                leds_ref[i].on() 
            else: 
                leds_ref[i].off() 
        if puls_7.is_pressed:
            jugador(0)
        if puls_16.is_pressed:
            jugador(1)
        if puls_17.is_pressed:
            jugador(2)
        if puls_19.is_pressed:
            jugador(3)

        contador = 0
        for i in range(4):
            if leds_jug[i].is_lit: 
                contador += 2**i
        if num == contador:
            reiniciar = True

# ej2
def main2():
    puls_7 = Button(7)
    puls_16 = Button(16)
    puls_17 = Button(17)
    puls_19 = Button(19)

    leds_jug = LEDBoard(24,25,26,27)
    leds_jug.off()
    leds_ref = [LED(20), LED(21), LED(22), LED(23)] 

    def jugador(i):
        leds_jug[i].toggle()

    reiniciar = True
    while True:
        if reiniciar:
            num = random.randint(1,15)
            reiniciar = False
        bits = [(num >> bit) & 0x1 for bit in range(4)] 

        ini = time.time()

        while time.time()-ini < 10:
            t_restante = 10 - (time.time()-ini)
            if puls_7.is_pressed:
                jugador(0)
            if puls_16.is_pressed:
                jugador(1)
            if puls_17.is_pressed:
                jugador(2)
            if puls_19.is_pressed:
                jugador(3)

            contador = 0
            for i in range(4):
                if leds_jug[i].is_lit: 
                    contador += 2**i
            if num == contador:
                print("Has acertado, se ha cambiado de numero")
                reiniciar = True
                break

            if t_restante >= 5:
                for i, bit in enumerate(bits): 
                    if bit == 1: 
                        leds_ref[i].on() 
                    else: 
                        leds_ref[i].off() 
            else:
                for i, bit in enumerate(bits): 
                    if bit == 1:  
                        leds_ref[i].on() 
                time.sleep(0.5)  
                for i, bit in enumerate(bits): 
                    if bit == 1:  
                        leds_ref[i].off() 
                time.sleep(0.5)

            time.sleep(1)
        
        if time.time() - ini >= 10 and num !=contador:
            print("Has perdido, se reinicia el contador")
            leds_jug.off()
            reiniciar = True

# ej3
def main2():
    puls_7 = Button(7)
    puls_16 = Button(16)
    puls_17 = Button(17)
    puls_19 = Button(19)

    leds_jug = LEDBoard(24,25,26,27)
    leds_jug.off()
    leds_ref = [LED(20), LED(21), LED(22), LED(23)] 

    def jugador(i):
        leds_jug[i].toggle()

    sensor = MCP3008(channel=7) 
    reiniciar = True
    while True:
        voltios = sensor.voltage
        lux = (voltios / 3.0) * 1500
        umbral = 1000
        if reiniciar:
            num = random.randint(1,15)
            reiniciar = False
        bits = [(num >> bit) & 0x1 for bit in range(4)] 

        if lux < umbral:
            time.sleep(1)
            for i in leds_ref:
                leds_ref[i].off()
        else:
            ini = time.time()

            while time.time()-ini < 10:
                t_restante = 10 - (time.time()-ini)
                if puls_7.is_pressed:
                    jugador(0)
                if puls_16.is_pressed:
                    jugador(1)
                if puls_17.is_pressed:
                    jugador(2)
                if puls_19.is_pressed:
                    jugador(3)

                contador = 0
                for i in range(4):
                    if leds_jug[i].is_lit: 
                        contador += 2**i
                if num == contador:
                    print("Has acertado, se ha cambiado de numero")
                    reiniciar = True
                    break

                if t_restante >= 5:
                    for i, bit in enumerate(bits): 
                        if bit == 1: 
                            leds_ref[i].on() 
                        else: 
                            leds_ref[i].off() 
                else:
                    for i, bit in enumerate(bits): 
                        if bit == 1:  
                            leds_ref[i].on() 
                    time.sleep(0.5)  
                    for i, bit in enumerate(bits): 
                        if bit == 1:  
                            leds_ref[i].off() 
                    time.sleep(0.5)

                time.sleep(1)
            
            if time.time() - ini >= 10 and num !=contador:
                print("Has perdido, se reinicia el contador")
                leds_jug.off()
                reiniciar = True