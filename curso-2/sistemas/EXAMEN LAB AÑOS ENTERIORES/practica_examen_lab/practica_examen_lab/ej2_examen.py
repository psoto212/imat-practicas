from gpiozero import LED, Button, PWMLED, LEDBoard
import time
from signal import pause
import threading

def main():
    leds = LEDBoard(20, 21, 22, 23, 24, pwm=True)
    leds_base = [PWMLED(25), PWMLED(26), PWMLED(27)] #utilizo pwmled para poder ajustar la intesidad 
    
    puls17 = Button(17)
    puls19 = Button(19)
    
    niveles = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    indice_nivel = 0  # Nivel inicial
    ultimo_nivel = 0  # Para restaurar el nivel después de la pulsación
    temporizador = None
    
    def disminuir():
        nonlocal indice_nivel, ultimo_nivel, temporizador
        if indice_nivel > 0:
            indice_nivel -= 1
            ultimo_nivel = indice_nivel
            nivel()
            reiniciar_temporizador()
        else:
            print("Error: Ya está apagado")
    
    def aumentar():
        nonlocal indice_nivel, ultimo_nivel, temporizador
        if indice_nivel < len(niveles) - 1:
            indice_nivel += 1
            ultimo_nivel = indice_nivel
            nivel()
            reiniciar_temporizador()
        else:
            print("Error: Nivel máximo alcanzado")
    
    def nivel():
        valor = niveles[indice_nivel]
        for i, led in enumerate(leds):
            if i < indice_nivel:
                led.on()
            else:
                led.off()
        for led in leds_base:
            led.value = valor
        print(f"Nivel de luminosidad: {int(valor * 100)}%")
    
    def apagado_gradual():
        nonlocal indice_nivel
        while indice_nivel > 0:
            time.sleep(2)
            indice_nivel -= 1
            nivel()
    
    def reiniciar_temporizador():
        nonlocal temporizador
        if temporizador:
            temporizador.cancel()
        temporizador = threading.Timer(5, apagado_gradual)
        temporizador.start()
    
    puls17.when_pressed = disminuir
    puls19.when_pressed = aumentar
    
    nivel()
    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
