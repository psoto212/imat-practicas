# ej1
from gpiozero import Button, LED, LEDBoard, PWMLED, MCP3008
from signal import pause
import time
import random

def main():
    leds_ref = [LED(20), LED(21), LED(22), LED(23)] 
    punto = Button(16)
    raya = Button(17)
    validar = Button(19)
    fallos = [LED(26),LED(27)]
    num_fallos = 0
    reiniciar = True
    morse = {10: [".", "-"], 11: ["-", ".", ".", "."], 12: ["-", ".", "-", "."], 13: ["-", ".", "."], 14: [".",], 15: [".", ".", "-", "."]}

    introducido = []
    def binario(num,leds):
        bits = [(num >> bit) & 0x1 for bit in range(len(leds))] 
        for i, bit in enumerate(bits): 
            if bit == 1: 
                leds[i].on() 
            else: 
                leds[i].off() 
    while True:
        if reiniciar:
            num = random.randint(10,15)
            reiniciar = False
        
        binario(num,leds_ref)
        if punto.is_pressed:
            introducido.append(".")
        if raya.is_pressed:
            introducido.append("-")
        if validar.is_pressed:
            if morse[num] == introducido:
                print("Has acertado")
                reiniciar = True
                introducido = []
                num_fallos = 0
            else:
                print("Has fallado")
                introducido = []
                if num_fallos < 3:
                    num_fallos += 1
                else:
                    print("has llegado al tope de fallos")
                    num_fallos = 3
                binario(num_fallos,fallos)

# ej2
def main():
    leds_ref = [PWMLED(20), PWMLED(21), PWMLED(22), PWMLED(23)] 
    punto = Button(16)
    raya = Button(17)
    validar = Button(19)
    fallos = [LED(26),LED(27)]
    num_fallos = 0
    reiniciar = True
    morse = {10: [".", "-"], 11: ["-", ".", ".", "."], 12: ["-", ".", "-", "."], 13: ["-", ".", "."], 14: [".",], 15: [".", ".", "-", "."]}
    intensidad = 1
    introducido = []
    puls1 = 0
    puls2 = 0
    def binario(num,leds,intensidad=1):
        bits = [(num >> bit) & 0x1 for bit in range(len(leds))] 
        for i, bit in enumerate(bits): 
            if bit == 1: 
                leds[i].value = intensidad
            else: 
                leds[i].off() 
    # no entiendo bien si lo que no puede durar mas de 4 s es el tiempo
    # transcurrido entre pulsar los dos botones de morse, o con el de validar
    # o con que
    # Lo he hecho haciendo que los 4 segundos sea entre los dos puls morse
    while True:
        if reiniciar:
            num = random.randint(10,15)
            reiniciar = False
        
        if punto.is_pressed:
            puls1 = time.time()
            introducido.append(".")
        if raya.is_pressed:
            puls2 = time.time()
            introducido.append("-")
        transcurrido = round(abs(puls1-puls2))
        if transcurrido < 4:
            intensidad = intensidad - round(transcurrido)*0.25
            binario(num,leds_ref,intensidad)
            puls1 = 0
            puls2 = 0
        else:
            print("se acabo el tiempo")
            if num_fallos < 3:
                    num_fallos += 1
            else:
                print("has llegado al tope de fallos")
                num_fallos = 3
            binario(num_fallos,fallos)
            puls1 = 0
            puls2 = 0
            binario(num,leds_ref)
        
        if validar.is_pressed:
            if morse[num] == introducido:
                print("Has acertado")
                reiniciar = True
                introducido = []
                num_fallos = 0
                
            else:
                print("Has fallado")
                introducido = []
                if num_fallos < 3:
                    num_fallos += 1
                else:
                    print("has llegado al tope de fallos")
                    num_fallos = 3
                binario(num_fallos,fallos)

# ej3
def main():
    sensor = MCP3008(channel=7)
    leds_ref = [PWMLED(20), PWMLED(21), PWMLED(22), PWMLED(23)] 
    punto = Button(16)
    raya = Button(17)
    validar = Button(19)
    fallos = [LED(26),LED(27)]
    num_fallos = 0
    reiniciar = True
    morse = {10: [".", "-"], 11: ["-", ".", ".", "."], 12: ["-", ".", "-", "."], 13: ["-", ".", "."], 14: [".",], 15: [".", ".", "-", "."]}
    intensidad = 1
    introducido = []
    puls1 = 0
    puls2 = 0
    def binario(num,leds,intensidad=1):
        bits = [(num >> bit) & 0x1 for bit in range(len(leds))] 
        for i, bit in enumerate(bits): 
            if bit == 1: 
                leds[i].value = intensidad
            else: 
                leds[i].off() 
    # no entiendo bien si lo que no puede durar mas de 4 s es el tiempo
    # transcurrido entre pulsar los dos botones de morse, o con el de validar
    # o con que
    # Lo he hecho haciendo que los 4 segundos sea entre los dos puls morse
    while True:
        voltios = sensor.voltage
        umbral = 240 # el que pusimos en la practica5
        # no entiendo lo del umbral si la tension va de 0 a 3.3 que deberia poner
        # MIRAR PRACTICA 5, ENTENDERLA MUY BIEN !!!!
        if reiniciar:
            num = random.randint(10,15)
            reiniciar = False
        
        if voltios*100 < umbral:
            introducido.append(".")
        else: 
            introducido.append("-")
        if punto.is_pressed:
            puls1 = time.time()
            introducido.append(".")
        if raya.is_pressed:
            puls2 = time.time()
            introducido.append("-")
        transcurrido = round(abs(puls1-puls2))
        if transcurrido < 4:
            intensidad = intensidad - round(transcurrido)*0.25
            binario(num,leds_ref,intensidad)
            puls1 = 0
            puls2 = 0
        else:
            print("se acabo el tiempo")
            if num_fallos < 3:
                    num_fallos += 1
            else:
                print("has llegado al tope de fallos")
                num_fallos = 3
            binario(num_fallos,fallos)
            puls1 = 0
            puls2 = 0
            binario(num,leds_ref)
        
        if validar.is_pressed:
            if morse[num] == introducido:
                print("Has acertado")
                reiniciar = True
                introducido = []
                num_fallos = 0
                
            else:
                print("Has fallado")
                introducido = []
                if num_fallos < 3:
                    num_fallos += 1
                else:
                    print("has llegado al tope de fallos")
                    num_fallos = 3
                binario(num_fallos,fallos)


