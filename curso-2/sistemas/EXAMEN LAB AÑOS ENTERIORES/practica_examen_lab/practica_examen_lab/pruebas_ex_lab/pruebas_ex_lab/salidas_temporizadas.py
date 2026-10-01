# ej1
from gpiozero import Button, LED, LEDBoard, PWMLED, MCP3008
from signal import pause
import time
import random

def main():
    desbloqueado = LED(27)
    bloqueado = LED(26)
    seguridad = Button(19)
    digito1 = LEDBoard(20,21)
    boton1 = Button(16)
    digito2 = LEDBoard(22,23)
    boton2 = Button(17)
    contador1 = 0
    contador2 = 0
    contra = []
    def iluminar(leds,contador):
        bits = [(contador >> bit) & 0x1 for bit in range(2)] 
        for i, bit in enumerate(bits): 
            if bit == 1: 
                leds[i].on() 
            else: 
                leds[i].off() 
    desbloqueado.on()
    while True:
        if boton1.is_pressed:
            contador1 = (contador1+1) % 4
            iluminar(digito1,contador1)
            time.sleep(0.2)
        if boton2.is_pressed:
            contador2 = (contador2+1) % 4
            iluminar(digito2,contador2)
            time.sleep(0.2)
        contadores = [contador1,contador2]

        if seguridad.is_pressed and not contra:
            print("Has bloqueado la maleta")
            contra = contadores
            contador1 = 0
            contador2 = 0
            desbloqueado.off()
            digito1.off()
            digito2.off()
            bloqueado.on()
        elif seguridad.is_pressed and contra:
            if contador1 == contra[0] and contador2 == contra[1]:
                print("Has debloqueado la maleta")
                contador1 = 0
                contador2 = 0
                desbloqueado.on()
                digito1.off()
                digito2.off()
                bloqueado.off()
            else: 
                print("no es la contraseña correcta")

            
# ej2
def main():
    desbloqueado = LED(27)
    bloqueado = PWMLED(26)
    seguridad = Button(19)
    digito1 = LEDBoard(20,21)
    boton1 = Button(16)
    digito2 = LEDBoard(22,23)
    boton2 = Button(17)
    contador1 = 0
    contador2 = 0
    contra = []
    pulsado = False
    intento = 0
    frecuencia = 0
    parpadeo = 1
    def iluminar(leds,contador):
        bits = [(contador >> bit) & 0x1 for bit in range(2)] 
        for i, bit in enumerate(bits): 
            if bit == 1: 
                leds[i].on() 
            else: 
                leds[i].off() 
    desbloqueado.on()
    while True:
        if boton1.is_pressed:
            if not pulsado:
                pulsado = True
                ini = time.time()
            contador1 = (contador1+1) % 4
            iluminar(digito1,contador1)
            time.sleep(0.2)
        if boton2.is_pressed:
            if not pulsado:
                pulsado = True
                ini = time.time()
            contador2 = (contador2+1) % 4
            iluminar(digito2,contador2)
            time.sleep(0.2)
        contadores = [contador1,contador2]

        if seguridad.is_pressed and not contra:
            print("Has bloqueado la maleta")
            contra = contadores
            contador1 = 0
            contador2 = 0
            desbloqueado.off()
            digito1.off()
            digito2.off()
            bloqueado.frequency = frecuencia
            bloqueado.duty_cycle = parpadeo
        
        if pulsado:
            if time.time() - ini > 10:
                print("¡Tiempo agotado! Fallo en el intento")
                intento += 1
                pulsado = False 
                if intento == 1:
                    frecuencia = 1  
                elif intento >= 2:
                    frecuencia = 2 
                bloqueado.frequency = frecuencia
                bloqueado.value = 0.5  
                continue

            if seguridad.is_pressed:
                if contador1 == contra[0] and contador2 == contra[1]:
                    print("¡Contraseña correcta! Has desbloqueado la maleta")
                    contador1 = 0
                    contador2 = 0
                    desbloqueado.on()
                    digito1.off()
                    digito2.off()
                    bloqueado.off()
                    pulsado = False
                    intento = 0  
                    frecuencia = 0
                    parpadeo = 1
                else:
                    print("Contraseña incorrecta")
                    intento += 1 
                    pulsado = False  
                    if intento == 1:
                        frecuencia = 1 
                    elif intento >= 2:
                        frecuencia = 2 
                    bloqueado.frequency = frecuencia
                    bloqueado.value = 0.5  

# ej3
def main():
    # divisor de tensor con resistencia de T media --> 470 O y
    # resistencia de eleccion --> 1kO, fuente de 3,3V
    umbral = 3.3*(470/(1000+470))
    sensor = MCP3008(channel=7)
    desbloqueado = LED(27)
    bloqueado = PWMLED(26)
    seguridad = Button(19)
    digito1 = LEDBoard(PWMLED(20),PWMLED(21))
    boton1 = Button(16)
    digito2 = LEDBoard(PWMLED(22),PWMLED(23))
    boton2 = Button(17)
    contador1 = 0
    contador2 = 0
    contra = []
    pulsado = False
    intento = 0
    frecuencia = 0
    parpadeo = 1
    def iluminar(leds, contador, brillo=1.0):
        bits = [(contador >> bit) & 0x1 for bit in range(2)] 
        for i, bit in enumerate(bits): 
            if bit == 1: 
                leds[i].frequency = 100  
                leds[i].value = brillo
            else: 
                leds[i].off() 

    desbloqueado.on()
    while True:
        voltios = sensor.voltage
        if voltios > umbral:
            brillo = 0.5
        else:
            brillo = 1.0
        if boton1.is_pressed:
            if not pulsado:
                pulsado = True
                ini = time.time()
            contador1 = (contador1 + 1) % 4
            iluminar(digito1, contador1, brillo)
            time.sleep(0.2)

        if boton2.is_pressed:
            if not pulsado:
                pulsado = True
                ini = time.time()
            contador2 = (contador2 + 1) % 4
            iluminar(digito2, contador2, brillo)
            time.sleep(0.2)

        contadores = [contador1, contador2]

        if seguridad.is_pressed and not contra:
            print("Has bloqueado la maleta")
            contra = contadores
            contador1 = 0
            contador2 = 0
            desbloqueado.off()
            digito1.off()
            digito2.off()
            bloqueado.frequency = frecuencia
            bloqueado.value = parpadeo
        
        if pulsado:
            if time.time() - ini > 10:
                print("¡Tiempo agotado! Fallo en el intento")
                intento += 1
                pulsado = False 
                if intento == 1:
                    frecuencia = 1  
                elif intento >= 2:
                    frecuencia = 2 
                bloqueado.frequency = frecuencia
                bloqueado.value = 0.5  
                continue

            if seguridad.is_pressed:
                if contador1 == contra[0] and contador2 == contra[1]:
                    print("¡Contraseña correcta! Has desbloqueado la maleta")
                    contador1 = 0
                    contador2 = 0
                    desbloqueado.on()
                    digito1.off()
                    digito2.off()
                    bloqueado.off()
                    pulsado = False
                    intento = 0  
                    frecuencia = 0
                    parpadeo = 1
                else:
                    print("Contraseña incorrecta")
                    intento += 1 
                    pulsado = False  
                    if intento == 1:
                        frecuencia = 1 
                    elif intento >= 2:
                        frecuencia = 2 
                    bloqueado.frequency = frecuencia
                    bloqueado.value = 0.5  

