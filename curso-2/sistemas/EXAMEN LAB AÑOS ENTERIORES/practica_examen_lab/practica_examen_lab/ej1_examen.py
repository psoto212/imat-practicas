from gpiozero import LED, Button, PWMLED, LEDBoard
import time
from signal import pause

def main():
    leds = LEDBoard(20, 21, 22, 23, 24, pwm=True)
    leds_base = [PWMLED(25), PWMLED(26), PWMLED(27)]
    
    puls17 = Button(17)
    puls19 = Button(19)
    
    niveles = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    indice_nivel = 0 

    def disminuir():
        nonlocal indice_nivel
        if indice_nivel > 0:
            indice_nivel -= 1
            nivel()
        else:
            print("Error: Ya está apagado")

    def aumentar():
        nonlocal indice_nivel
        if indice_nivel < len(niveles) - 1:
            indice_nivel += 1
            nivel()
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
    
    puls17.when_pressed = disminuir
    puls19.when_pressed = aumentar
    
    nivel()
    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
