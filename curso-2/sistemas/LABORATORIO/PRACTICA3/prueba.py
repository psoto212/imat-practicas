from gpiozero import LED, Button
from time import sleep
import random


comun = False
def main():
    
    pines_auto = (20, 21, 22, 23)
    leds_auto = [LED(pin) for pin in pines_auto]

    pines_manu = (24,25,26,27)
    leds_auto = [LED(pin) for pin in pines_manu]



    boton_7  = Button(7,  pull_up=True)  
    boton_19  = Button(19,  pull_up=True)  
    boton_16 = Button(16, pull_up=True)
    boton_17 = Button(17, pull_up=True)

    numero_aleatorio = {"val": random.randint(0,15)}

    def mostrar():
        bits = [(numero_aleatorio["val"] >> bit) & 1 for bit in range(4)]
        leds_auto.value = bits
        print("numero_aleatorio =", numero_aleatorio["val"], "bits =", bits)


    def poner_en_comun():
        global comun
        if boton_7.is_pressed:
            LED(24).on
        if boton_16.is_pressed:
            LED(25).on
        if boton_17.is_pressed:
            LED(26).on
        if boton_19.is_pressed:
            LED(27).on


        if (LED(24).value == LED(20).value) and (LED(25).value == LED(21).value) and (LED(26).value == LED(22).value) and (LED(27).value == LED(23).value):
            comun = not comun

            if comun:
                for i in range(leds_auto):
                    leds_auto[i].off
                    for j in range(leds_manu):
                        leds_manu[j].off


    while True:
            sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")




        


            




