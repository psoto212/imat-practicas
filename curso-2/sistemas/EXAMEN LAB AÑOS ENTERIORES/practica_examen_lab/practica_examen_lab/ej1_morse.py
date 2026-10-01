import random
from gpiozero import Button, LED
from signal import pause
import time

contador = random.randint(10,15)
print(contador)
contador2 = 0
respuesta = ""

def main():

    leds_referencia = [LED(20), LED(21), LED(22), LED(23)]
    leds_fallos = [LED(26), LED(27)]
    button19 = Button(19)
    button17 = Button(17)
    button16 = Button(16)

    def actualizar_leds():
        bits = [(contador >> bit) & 0x1 for bit in range(4)]
        for i, bit in enumerate(bits):
            if bit == 1:
                leds_referencia[i].on()
            else:
                leds_referencia[i].off()

    def actualizar_fallos():
        bits = [(contador2 >> bit) & 0x1 for bit in range(2)]
        for i, bit in enumerate(bits):
            if bit == 1:
                leds_fallos[i].on()
            else:
                leds_fallos[i].off()



    def confirmar():
        global contador, contador2, respuesta
        contador = random.randint(10, 15)
        print(contador)
        time.sleep(1)  # Pausa antes de reiniciar
        contador2 = 0
        respuesta = ""
        actualizar_leds()
        actualizar_fallos()

    def validar():
        global respuesta, contador2
        
        respuestas = {10: ".-", 11: "-...", 12: "-.-.", 13: "-..", 14:".", 15: "..-."}

        if respuestas[contador] == respuesta:
            print("has acertado empezamos de nuevo ")
            confirmar()
        else:
            if contador2 < 3:
                contador2 += 1
                actualizar_fallos()
                print("joooo, has fallado se reinicia la respuesta ")
            elif contador2 == 3:
                print("El recuento de fallos se ha saturado, pero la partida continua")  
            respuesta = ""


    def respuesta_punto():
        global respuesta
        respuesta += "."
        print(respuesta)

    def respuesta_raya():
        global respuesta
        respuesta += "-"
        print(respuesta)


    actualizar_leds()
    actualizar_fallos()

    button19.when_pressed= validar
    button17.when_pressed = respuesta_raya
    button16.when_pressed = respuesta_punto

    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
