from gpiozero import LEDBoard, Button, LED
from time import sleep

pines_pista = [x for x in range(24, 28)]
leds_pista = LEDBoard(*pines_pista, pwm=True)

jugando = False
pos_jugador = 0      # GPIO24
pos_meta = 3         # GPIO27
puntuacion = 0

led_final = LED(21)
led_punto = LED(20)

val_meta = 0.4

boton_corredor = Button(16, pull_up=True)
boton_meta = Button(19, pull_up=True)
boton_reset = Button(17, pull_up=True)


def main():
    global jugando, pos_jugador, pos_meta, puntuacion

    def mostrar():
        leds_pista.off()

        # Meta al 40%
        leds_pista[pos_meta].value = val_meta

        # Jugador al 100%; si coinciden, manda el jugador
        leds_pista[pos_jugador].value = 1.0

    def parpadear_punto():
        led_punto.on()
        sleep(0.2)
        led_punto.off()

    def recolocar_meta():
        global pos_meta
        pos_meta = (pos_jugador + 2) % 4
        if pos_meta == pos_jugador:
            pos_meta = (pos_meta + 1) % 4

    def comprobar_punto():
        global puntuacion, jugando

        if pos_jugador == pos_meta:
            puntuacion += 1
            parpadear_punto()

            if puntuacion >= 3:
                jugando = False
                leds_pista.off()
                led_final.on()
            else:
                recolocar_meta()
                mostrar()

    def avanzar_jugador():
        global pos_jugador

        if not jugando:
            return

        pos_jugador = (pos_jugador + 1) % 4
        mostrar()
        comprobar_punto()

    def avanzar_meta():
        global pos_meta

        if not jugando:
            return

        pos_meta = (pos_meta - 1) % 4
        mostrar()
        comprobar_punto()

    def reset():
        global jugando, pos_jugador, pos_meta, puntuacion

        jugando = True
        pos_jugador = 0
        pos_meta = 3
        puntuacion = 0

        led_final.off()
        led_punto.off()
        mostrar()

    boton_corredor.when_pressed = avanzar_jugador
    boton_meta.when_pressed = avanzar_meta
    boton_reset.when_pressed = reset

    reset()

    while True:
        sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")