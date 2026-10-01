import random
from gpiozero import Button, LED
from signal import pause
import time
from threading import Thread

def main():
    contador = random.randint(0, 15)
    
    leds_referencia = [LED(20), LED(21), LED(22), LED(23)]
    leds_base = [LED(24), LED(25), LED(26), LED(27)]

    puls_24 = Button(7)
    puls_25 = Button(16)
    puls_26 = Button(17)
    puls_27 = Button(19)

    inicio = time.time()  # Se guarda el tiempo de inicio

    def actualizar_leds():
        """ Actualiza los LEDs de referencia según el número aleatorio. """
        bits = [(contador >> bit) & 0x1 for bit in range(4)]
        for i, bit in enumerate(bits):
            if bit == 1:
                leds_referencia[i].on()
            else:
                leds_referencia[i].off()

    def enceder_24():
        leds_base[0].toggle()
        salir()

    def enceder_25():
        leds_base[1].toggle()
        salir()

    def enceder_26():
        leds_base[2].toggle()
        salir()

    def enceder_27():
        leds_base[3].toggle()
        salir()

    def salir():
        global igual
        igual = all(led1.is_lit == led2.is_lit for led1, led2 in zip(leds_referencia, leds_base))
        
        if igual:
            cambiar_numero()

    def cambiar_numero():
        """ Genera un nuevo número aleatorio y reinicia los LEDs. """
        nonlocal contador, inicio
        contador = random.randint(0, 15)
        time.sleep(1)  # Pausa antes de reiniciar
        for led in leds_base:
            led.off()
        for led in leds_referencia:
            led.off()
        inicio = time.time()  # Se reinicia el tiempo solo aquí
        actualizar_leds()
    
    def parpadeo():
        """ Maneja la cuenta regresiva y el parpadeo de los LEDs de referencia. """
        while True:
            tiempo_restante = 10 - (time.time() - inicio)  # Cuenta regresiva

            if tiempo_restante <= 0:
                cambiar_numero()  # Se acabó el tiempo, se reinicia el número
            elif tiempo_restante <= 5:
                # Cuando queden menos de 5 segundos, los LEDs de referencia encendidos parpadean a 1 Hz
                for led in leds_referencia:
                    if led.is_lit:
                        led.blink(on_time=0.5, off_time=0.5)
            else:
                # Si aún hay más de 5 segundos, asegurarse de que los LEDs de referencia están normales
                for led in leds_referencia:
                    if led.is_lit:
                        led.on()
            
            time.sleep(1)  # Revisar el tiempo cada segundo

    # Iniciar el hilo para la cuenta regresiva sin bloquear el programa principal
    hilo_tiempo = Thread(target=parpadeo, daemon=True)
    hilo_tiempo.start()

    actualizar_leds()

    puls_24.when_pressed = enceder_24
    puls_25.when_pressed = enceder_25
    puls_26.when_pressed = enceder_26
    puls_27.when_pressed = enceder_27

    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
