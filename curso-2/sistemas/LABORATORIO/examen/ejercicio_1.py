from gpiozero import LEDBoard, Button, LED
from time import sleep
import random


def main():
    led_vivo = LED(27)
    leds = LEDBoard(21, 22, 23, 24, 25)
    leds_totales =5   

    boton_subir = Button(16)
    boton_disparo = Button(19)
    boton_vivir = Button(17)

    contador_disparos = 0
    contador = 0
    balas = 3
    subiendo = False


    boton_subir_anterior = False
    boton_disparo_anterior = False
    boton_vivir_anterior = False


        
    def led_objetivo():
        for led in leds:
            numero_objetivo = random.randint(1,5)
            leds[numero_objetivo].on()



    while True:
        b16 = boton_subir.is_pressed
        b19 = boton_disparo.is_pressed
        b17 = boton_vivir.is_pressed

        if b16 and not boton_subir_anterior:
            for i in range(leds_totales):
                subiendo = True
                if i < 5:
                    led_cazador = leds[contador]
                    led_cazador.on()
                    contador += 1
                else:
                    subiendo = False

                if not subiendo:
                    subiendo = False
                    if i>0:
                        led_cazador = leds[contador]
                        led_cazador.on()
                        contador -= 1
                    else:
                        subiendo = True
            


        if b19 and not boton_disparo_anterior:
            if led_objetivo == led_cazador:
                print("CAZADO!")
            else:
                balas -= 1
                if balas > 0:
                    print(f"Fallo!, le quedan {balas} balas restantes")
                else:
                    print("Muerto!")
                    led_vivo.off()

        if b17 and not boton_vivir_anterior:
            for i in range(0,1):
                leds[i].on()
            led_vivo.on()
            led_objetivo()



        boton_subir_anterior = b16
        boton_disparo_anterior = b19
        boton_vivir_anterior = b17

        sleep(0.05)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")





        


            





        



        

            
            

            

        

            
            



            








