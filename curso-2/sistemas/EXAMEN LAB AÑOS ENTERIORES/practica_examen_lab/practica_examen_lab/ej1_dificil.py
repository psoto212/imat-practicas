from gpiozero import Button, LEDBoard
from signal import pause
from time import sleep

leds = LEDBoard(20,21,22,23,24,25,26,27)
boton = Button(19)

def funcion_encender():
    numero1 = 0
    numero2 = 1

    for i in range(12):
        actual = numero1 + numero2
        numero1 = numero2
        numero2 = actual 
        actual_binario = str(bin(actual)[2:])


        while len(actual_binario)!= 8:
            actual_binario+="0"
        

        for i in range(8):
            if actual_binario[i] == "1":
                leds[i].on()
            else:
                leds[i].off()
        sleep(1) 

    leds.off()

boton.when_pressed = funcion_encender

pause()