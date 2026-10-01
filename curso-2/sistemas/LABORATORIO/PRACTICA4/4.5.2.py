from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause
import threading

abierto = False
timer = None

CERRADO = -45
ABIERTO = 45
AUTO_CLOSE_S = 10

def cerrar_barrera(servo: AngularServo) -> None:
    global abierto, timer
    servo.angle = CERRADO
    abierto = False
    timer = None  # ya se ejecutó

def cambiar_posicion(servo: AngularServo) -> None:
    global abierto, timer

    if abierto:
        servo.angle = CERRADO
        if timer is not None:
            timer.cancel()
            timer = None
        abierto = False
    else:
        servo.angle = ABIERTO
        timer = threading.Timer(AUTO_CLOSE_S, cerrar_barrera, args=(servo,))
        timer.start()
        abierto = True

def main() -> None:
    factory = PiGPIOFactory()

    servo = AngularServo(
        14,
        min_pulse_width=0.5e-3,
        max_pulse_width=2.5e-3,
        pin_factory=factory
    )

    # pull_up=True típico: botón a GND => pulsado = LOW
    boton = Button(19, pull_up=True)

    servo.angle = CERRADO

    boton.when_pressed = lambda: cambiar_posicion(servo)

    pause()  # mantiene el programa vivo sin gastar CPU

if __name__ == "__main__":
    main()