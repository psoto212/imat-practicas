from gpiozero import LEDBoard, Button, LED, PWMLED
from time import sleep


def main():
    leds = LEDBoard(24, 25, 26, 27)
    led_riego = LED(21)
    led_distancia_inf = PWMLED(20)
    led_distancia_sup = PWMLED(22)

    boton_16 = Button(16)
    boton_17 = Button(17)
    boton_19 = Button(19)

    niveles = 2
    humedad_nivel = 0.5
    humedad = 0.4

    def mostrar():
        nonlocal niveles
        for i in range(4):
            if i < niveles:
                leds[i].on()
            else:
                leds[i].off()

    def botonear_16():
        nonlocal niveles, humedad_nivel
        niveles = 0
        humedad_nivel = 0
        mostrar()
        print("reiniciado")

    def botonear_17():
        nonlocal niveles, humedad_nivel
        if niveles > 0:
            niveles -= 1
            humedad_nivel -= 0.25
            if humedad_nivel < 0:
                humedad_nivel = 0
            mostrar()
            print("disminuyó")
            print("niveles:", niveles)
            print("humedad_nivel:", humedad_nivel)

    def botonear_19():
        nonlocal niveles, humedad_nivel
        if niveles < 4:
            niveles += 1
            humedad_nivel += 0.25
            if humedad_nivel > 1:
                humedad_nivel = 1
            mostrar()
            print("aumentó")
            print("niveles:", niveles)
            print("humedad_nivel:", humedad_nivel)

    boton_16.when_pressed = botonear_16
    boton_17.when_pressed = botonear_17
    boton_19.when_pressed = botonear_19

    mostrar()

    while True:
        if niveles > 1:
            if humedad < humedad_nivel:
                humedad_valor = humedad_nivel - humedad
                led_distancia_inf.value = humedad_valor
                led_distancia_sup.value = 0
                led_riego.on()

            elif humedad > humedad_nivel:
                humedad_valor = humedad - humedad_nivel
                led_distancia_sup.value = humedad_valor
                led_distancia_inf.value = 0
                led_riego.off()

            else:
                led_distancia_inf.value = 0
                led_distancia_sup.value = 0
                led_riego.off()

        elif niveles == 1:
            led_riego.off()
            led_distancia_inf.value = 0
            led_distancia_sup.value = 0
            mostrar()

        else:
            leds.off()
            led_riego.off()
            led_distancia_inf.value = 0
            led_distancia_sup.value = 0

        sleep(0.01)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")