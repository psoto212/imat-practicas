from gpiozero import LED, Button, PWMLED
import random
import time
from signal import pause


def reinicio(v):
    global cuenta1, cuenta2
    if v == 1:
        led_desbloqueado.on()
        led_activacion.off()
        for i in range(2):
            leds_16[i].off()
            leds_17[i].off()
        cuenta1 = 0
        cuenta2 = 0

    elif v == 2:
        led_desbloqueado.off()
        led_activacion.on()
        for i in range(2):
            leds_16[i].off()
            leds_17[i].off()
        cuenta1 = 0
        cuenta2 = 0

    else:
        cuenta1 = 0
        cuenta2 = 0
        for i in range(2):
            leds_16[i].off()
            leds_17[i].off()

  
def pulsador1():
    global cuenta1, pulsa_16_17
    if pulsa_16_17 == 0:
        pulsa_16_17 = time.time 
    if cuenta1 > 3:
        reinicio(3)
        print("has desbordado vuelve al inicio")
    else:
        cuenta1 +=1
        actualizar_leds_1()

def pulsador2():
    global cuenta2, pulsa_16_17
    
    if pulsa_16_17 == 0:
        pulsa_16_17 = time.time 
    if cuenta2 > 3:
        reinicio(3)
        print("has desbordado vuelve al inicio")
    else:
        cuenta2+= 1
        actualizar_leds_2()

def actualizar_leds_1():
    bits = [(cuenta1 >> bit) & 0x1 for bit in range(2)]
    for i, estado in enumerate(bits):
        if estado:
            leds_16[i].on()
        else:
            leds_16[i].off()

def actualizar_leds_2():
    bits = [(cuenta2 >> bit) & 0x1 for bit in range(2)]
    for i, estado in enumerate(bits):
        if estado:
            leds_17[i].on()
        else:
            leds_17[i].off()

def activar():
    global respuesta, contrasena, activar_bien, fallo

    if activar_bien:
        respuesta.append(cuenta1)
        respuesta.append(cuenta2)
        reinicio(2)
        activar_bien = False

    else:
        contrasena.append(cuenta1)
        contrasena.append(cuenta2)
        ok = True
        for i in range(2):
            if contrasena[i] != respuesta[i]:
                ok = False

        if ok:
            reinicio(1)
            activar_bien = True
            print("enhorabuena todo ha ido genial vuelve a empezar")
        else:
            if not fallo:
                fallo = True
                print("Ha fallado pero no se reinciaran los contadores")
            else:
                fallo = False
                activar_bien = True
                print("oooo hemos fallado vuelta a empezar")
                reinicio(3)

def fallos():
    global numero_fallos, inicio


    if numero_fallos == 1:
        if led_activacion.is_lit:
            print("han  pasado ya 10 segundos")
            led_activacion.blink(on_time= 0.5, off_time=0.5)


    elif numero_fallos == 2:
        if led_activacion.is_lit:
            print("han pasado ya 20 segundos")
            led_activacion.blink(on_time= 0.25, off_time=0.25)
    else:
        print("esta tardando mucho")



try:
    puls16 = Button(16)
    puls17 = Button(17)
    puls19 = Button(19)

    leds_16 = [LED(20), LED(21)]
    leds_17 = [LED(22), LED(23)]

    led_desbloqueado = LED(27)
    led_activacion = LED(26)


    cuenta1 = 0
    cuenta2 = 0
    respuesta = []
    contrasena = []

    reinicio(1)
    activar_bien = True
    fallo = False
    numero_fallos = 0

    pulsa_16_17 = time.time()
    inicio = time.time()


    puls16.when_pressed = pulsador1
    puls17.when_pressed = pulsador2
    puls19.when_pressed = activar


    pause()

except KeyboardInterrupt:
    pass

