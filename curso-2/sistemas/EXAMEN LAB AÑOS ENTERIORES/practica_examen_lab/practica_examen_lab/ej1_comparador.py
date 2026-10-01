# import random
# from gpiozero import Button, LEDBoard, LED
# from signal import pause

# def main():
#     contador = random.randint(0,15)
#     leds_referencia = [LED(20), LED(21), LED(22), LED(23)]
#     leds_base = [LED(24), LED(25), LED(26), LED(27)]


#     puls_24 = Button(7)
#     puls_25 = Button(16)
#     puls_26 = Button(17)
#     puls_27 = Button(19)

#     igual  = False

#     def actualizar_leds():
#             bits = [(contador >> bit) & 0x1 for bit in range(4)]
#             for i, bit in enumerate(bits):
#                 if bit == 1:
#                     leds_referencia[i].on()
#                 else:
#                     leds_referencia[i].off()

#     def enceder_24():
#         leds_base[0].toggle()
#         salir() 

#     def enceder_25():
#         leds_base[1].toggle()
#         salir() 

#     def enceder_26():
#         leds_base[2].toggle()
#         salir() 
        
#     def enceder_27():
#         leds_base[3].toggle()
#         salir() 


#     def salir():
#         global igual
#         for led1, led2 in zip(leds_referencia, leds_base):
#             if led1.is_lit == led2.is_lit:
#                 igual = True
#             else: 
#                 igual = False
#         if igual == True:
#             cambiar_numero()
            

#     def cambiar_numero():
#         nonlocal contador
#         if igual == True:
#             contador = random.randint(0,15)
#             for led in leds_base:
#                 led.off()

#             actualizar_leds()


#     actualizar_leds()
#     puls_24.when_pressed = enceder_24
#     puls_25.when_pressed = enceder_25
#     puls_26.when_pressed = enceder_26
#     puls_27.when_pressed = enceder_27


#     pause()

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         pass



import random
from gpiozero import Button, LED
from signal import pause
import time

def main():
    contador = random.randint(0, 15)

    # Definir LEDs
    leds_referencia = [LED(20), LED(21), LED(22), LED(23)]
    leds_base = [LED(24), LED(25), LED(26), LED(27)]

    # Definir botones
    puls_24 = Button(7)
    puls_25 = Button(16)
    puls_26 = Button(17)
    puls_27 = Button(19)

    # Función para actualizar los LEDs de referencia según el número aleatorio
    def actualizar_leds():
        bits = [(contador >> bit) & 0x1 for bit in range(4)]
        for i, bit in enumerate(bits):
            leds_referencia[i].value = bit  # 1 = encendido, 0 = apagado

    # Función para alternar los LEDs de la base
    def encender_led(index):
        leds_base[index].toggle()
        verificar_igualdad()

    # Función para verificar si los LEDs de base coinciden con los de referencia
    def verificar_igualdad():
        if all(led1.is_lit == led2.is_lit for led1, led2 in zip(leds_referencia, leds_base)):
            cambiar_numero()

    # Función para generar un nuevo número y reiniciar los LEDs de base
    def cambiar_numero():
        nonlocal contador
        time.sleep(1)
        contador = random.randint(0, 15)

        # Apagar todos los LEDs de la base antes de actualizar
        for led in leds_base:
            led.off()

        actualizar_leds()

    # Inicializar los LEDs de referencia
    actualizar_leds()

    # Asignar funciones a los botones
    puls_24.when_pressed = lambda: encender_led(0)
    puls_25.when_pressed = lambda: encender_led(1)
    puls_26.when_pressed = lambda: encender_led(2)
    puls_27.when_pressed = lambda: encender_led(3)

    pause()  # Mantener el script en ejecución

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
