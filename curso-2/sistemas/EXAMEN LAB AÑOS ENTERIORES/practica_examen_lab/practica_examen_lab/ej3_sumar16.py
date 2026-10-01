import random
from gpiozero import Button, LED
from signal import pause
import time
import spidev  # Para leer el ADC MCP3008

def read_potentiometer():
    spi = spidev.SpiDev()
    spi.open(0, 0)  # SPI bus 0, dispositivo 0
    spi.max_speed_hz = 1350000
    adc = spi.xfer2([1, (8) << 4, 0])  # Leer canal 0 del MCP3008
    value = ((adc[1] & 3) << 8) + adc[2]
    spi.close()
    return (value / 1023.0) * 3.3  # Convertir a voltaje (0V - 3.3V)

def calcular_tiempo_intento():
    voltaje = read_potentiometer()
    return 2 + (voltaje / 3.3) * 6  # Interpola entre 2s y 8s

def main():
    leds_referencia = [LED(20), LED(21), LED(22), LED(23)]
    leds_jugador = [LED(24), LED(25), LED(26), LED(27)]
    puls_16 = Button(16)
    puls_17 = Button(17)
    puls_19 = Button(19)
    
    def actualizar_leds_referencia():
        for led in leds_referencia:
            led.off()
        bits = [(numero >> bit) & 0x1 for bit in range(4)]
        for i, estado in enumerate(bits):
            if estado:
                leds_referencia[i].on()
            else:
                leds_referencia[i].off()
    
    def actualizar_leds_jugador():
        bits = [(numero_jugador >> bit) & 0x1 for bit in range(4)]
        for i, estado in enumerate(bits):
            if estado:
                leds_jugador[i].on()
            else:
                leds_jugador[i].off()
    
    def sumar():
        global numero_jugador
        if numero_jugador < 15:
            numero_jugador += 1
            actualizar_leds_jugador()
    
    def restar():
        global numero_jugador
        if numero_jugador > 0:
            numero_jugador -= 1
            actualizar_leds_jugador()
    
    def comprobar():
        global numero, intentos, tiempo_intento
        intentos += 1
        if numero + numero_jugador == 16 or intentos == 3:
            numero = random.randint(0, 15)
            intentos = 0
            tiempo_intento = calcular_tiempo_intento()
            actualizar_leds_referencia()
        else:
            if intentos == 1:
                for led in leds_referencia:
                    led.blink(on_time=0.25, off_time=0.25)
            elif intentos == 2:
                for led in leds_referencia:
                    led.blink(on_time=0.125, off_time=0.125)
        
    def temporizador():
        global intentos, tiempo_intento
        while True:
            time.sleep(tiempo_intento)
            if numero + numero_jugador != 16:
                comprobar()
    
    numero_jugador = 0
    numero = random.randint(1, 15)
    intentos = 0
    tiempo_intento = calcular_tiempo_intento()
    actualizar_leds_referencia()
    
    puls_16.when_pressed = sumar
    puls_17.when_pressed = restar
    puls_19.when_pressed = comprobar
    
    from threading import Thread
    thread = Thread(target=temporizador)
    thread.daemon = True
    thread.start()
    
    pause()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
