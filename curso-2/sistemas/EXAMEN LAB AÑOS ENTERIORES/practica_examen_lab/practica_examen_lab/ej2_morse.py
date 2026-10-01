from gpiozero import LED, Button, PWMLED
import random
import time

puls16 = Button(16)
puls17 = Button(17)
puls19 = Button(19)

led_pins1 = [20, 21, 22, 23]
led_pins2 = [26, 27]

# leds1 = [LED(pin) for pin in led_pins1]
leds1 = [PWMLED(pin) for pin in led_pins1] #PWLED(pin) en vez de la otra clase porque ahora vamos a multiplicar por la intensidad(1, 0.75, 0.50, 0.25)
leds2 = [LED(pin) for pin in led_pins2]

morse_dic = {10: ".-", 11: "-...", 12: "-.-.", 13: "-..", 14:".", 15: "..-."}

def actualizar_leds(numero):      
    bits = [(numero >> bit) & 0x1 for bit in range(4)] # Los bits van de menor a
    for i, estado in enumerate(bits):  
        if estado:  
            leds1[i].on()  
        else:  
            leds1[i].off()  

def actualizar_fallos(fallos):      
    bits = [(fallos >> bit) & 0x1 for bit in range(2)]
    for i, estado in enumerate(bits):  
        if estado:  
            leds2[i].on()  
        else:  
            leds2[i].off()  

def anadir_punto():
    global respuesta_user, ultima_pulsacion, numero
    ultima_pulsacion = time.time()
    respuesta_user += "."
    print("añado punto", respuesta_user)
    actualizar_leds(numero)

def anadir_ralla():
    global respuesta_user, ultima_pulsacion, numero
    ultima_pulsacion = time.time()
    respuesta_user += "-"
    print("añado ralla", respuesta_user)
    actualizar_leds(numero)
   
def validar():
    global respuesta, respuesta_user, solucionado, fallos, ultima_pulsacion, numero
    ultima_pulsacion = time.time()
    #quiere comprobar respuesta
    if respuesta_user == respuesta:
        print("Muy bien, has solucionado el ejercicio")
        print("Generamos nuevo numero y partida")
        solucionado = True
    else:
        respuesta_user = ""
        print("Respuesta incorrecta, sumamos un fallo. Reinciamos tu respuesta, sigue intentandolo")
        if fallos < 3:
            fallos += 1
            actualizar_leds(numero)
        if fallos == 3:
            print("El recuento de fallos se ha saturado, pero la partida continua")      

try:
    tiempo_un_seg = time.time()
    ultima_pulsacion = time.time()
    while True:
        numero = random.randint(10,15)
        actualizar_leds(numero)
        respuesta = morse_dic[numero]
        print("RESPUESTA: ", numero, respuesta)

        fallos = 0
        respuesta_user = ""

        solucionado = False
        while not solucionado:
            actualizar_fallos(fallos)

            puls16.when_pressed = anadir_punto
            puls17.when_pressed = anadir_ralla
            puls19.when_pressed = validar

            if (time.time() - ultima_pulsacion) > 4:
                print("Han pasado 4 segundos desde la ultima pulsacion, añadimos un fallo")
                actualizar_leds(numero)
                #añado fallo y cambio ultima pulsacion a este momento para volver a contar el tiempo
                if fallos <3:
                    fallos += 1
                ultima_pulsacion = time.time()
        
        
            if (time.time() - tiempo_un_seg) >= 1:
                for led in leds1:
                    if led.value>0:
                        print("imprimo el led value" , led.value)
                        led.value -= 0.25 #resto 0.25 para que disminuya un 25%
                # ahora tengo que actualizar la variable tiempo_un_seg
                tiempo_un_seg = time.time()
                
except KeyboardInterrupt:
    print("Limpieza de LEDs y salida del programa.")