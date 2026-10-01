from gpiozero import LEDBoard, Button, LED, PWMLED
from time import sleep, time



leds_normales = LEDBoard(20,21,22,23)

boton_19 = Button(19)
boton_17 = Button(17)
boton_16 = Button(16)

estado = {"modo": "BLOQUEADO",
          "objetivo" : ["A","B","A"],
          "secuencia" : []}


def main():
    def mostrar():
        leds_normales.off()
        if estado["modo"] == "ABIERTO":
            leds_normales[3].on()


        if estado["modo"] == "BLOQUEADO":
            for i in range(len(estado["secuencia"])):
                leds_normales[i].on()
        if estado["modo"] == "ERROR":
            leds_normales.on()
            sleep(0.2)
            leds_normales.off()
            sleep(0.2)
            estado["modo"] = "BLOQUEADO"

    def parpadear(veces):
        for _ in range(veces):
            leds_normales.on()
            sleep(0.2)
            leds_normales.off()
            sleep(0.2)

    def reset():
        if estado["modo"] == "BLOQUEADO":
            estado["modo"] = "BLOQUEADO"
            estado["secuencia"] = []
        else:
            estado["modo"] = "BLOQUEADO"
            estado["secuencia"] = []

    def comprobar():
        if len(estado["objetivo"]) == len(estado["secuencia"]) and estado["objetivo"] == estado["secuencia"]:
            estado["modo"] = "ABIERTO"
            mostrar()

        if len(estado["objetivo"]) == len(estado["secuencia"]) and not  estado["objetivo"] == estado["secuencia"]:
            estado["modo"] = "BLOQUEADO"
            mostrar()
            reset()


        
            

    def botonear_19():
        if estado["modo"] == "BLOQUEADO":
            estado["secuencia"].append("A")
            mostrar()
            comprobar()

    def botonear_17():
        if estado["modo"] == "BLOQUEADO":
            estado["secuencia"].append("B")
            mostrar()
            comprobar()


    

    boton_16.when_pressed = reset
    boton_19.when_pressed = botonear_19
    boton_17.when_pressed = botonear_17



    while True:
        sleep(0.01)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")





    








    


