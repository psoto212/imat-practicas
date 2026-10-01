import random
from gpiozero import Button, LED
from signal import pause
import time
from threading import Thread

def main():
    
    leds_referencia = [LED(20), LED(21), LED(22), LED(23)]
    leds_jugador = [LED(24), LED(25), LED(26), LED(27)]

    
    puls_16= Button(16)
    puls_17 = Button(17)
    puls_19 = Button(19)



    def actualizar_leds_referencia():
        for led in leds_referencia:
            led.off()  # Apagar LEDs antes de actualizar (detiene parpadeo)
        bits = [(numero >> bit) & 0x1 for bit in range(4)]
        for i, estado in enumerate(bits):
            if estado:
                leds_referencia[i].on()
            else:
                leds_referencia[i].off()
    
    
    def actualizar_leds_jugador():
        bits = [(numero_jugador >> bit) & 0x1 for bit in range(4)]
        for i, estado in enumerate(bits):
            if estado:
                leds_jugador[i].on()
            else:
                leds_jugador[i].off()
    
    def sumar():
        global numero_jugador
        if numero_jugador < 15:
            numero_jugador += 1
            actualizar_leds_jugador()

    
    def restar():
        global numero_jugador
        if numero_jugador > 0:
          numero_jugador -= 1
          actualizar_leds_jugador()
     
    def comprobar():
        global numero, intentos
        intentos += 1
        if numero + numero_jugador == 16 or intentos == 3:
            numero = random.randint(0,15)
            intentos = 0
            actualizar_leds_referencia()
            
        else:
            if intentos == 1:
                for i in range(4):
                    if leds_referencia[i].is_lit():
                        leds_referencia[i].blink(on_time = 0.25, off_time = 0.25)
            elif intentos == 2:
                for i in range(4):
                    if leds_referencia[i].is_lit():
                        leds_referencia[i].blink(on_time = 0.125, off_time = 0.125)


    numero_jugador = 0
    numero = random.randint(1,15)
    intentos = 0
    actualizar_leds_referencia()

    puls_16.when_pressed = sumar
    puls_17.when_pressed = restar
    puls_19.when_pressed = comprobar

    pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
