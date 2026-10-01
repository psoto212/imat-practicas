from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory
from threading import Timer
from signal import pause

abierto = False
temporizador = None

CERRADO = -45
ABIERTO = 45

def main():
    global abierto, temporizador

    factory = PiGPIOFactory()

    servo = AngularServo(
        14,
        min_pulse_width=0.0005,
        max_pulse_width=0.0025,
        min_angle=-90,
        max_angle=90,
        pin_factory=factory
    )

    boton_abrir = Button(19, pull_up=True)
    boton_cerrar = Button(17, pull_up=True)

    def cancelar_temporizador():
        global temporizador
        if temporizador is not None:
            temporizador.cancel()
            temporizador = None

    def autocerrar():
        global abierto, temporizador
        servo.angle = CERRADO
        abierto = False
        temporizador = None

    def cerrar():
        global abierto
        cancelar_temporizador()
        servo.angle = CERRADO
        abierto = False

    def abrir():
        global abierto, temporizador
        servo.angle = ABIERTO
        abierto = True

        cancelar_temporizador()
        temporizador = Timer(5.0, autocerrar)
        temporizador.start()

    cerrar()

    boton_abrir.when_pressed = abrir
    boton_cerrar.when_pressed = cerrar

    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass