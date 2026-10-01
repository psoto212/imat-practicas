from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time

# Variables globales
abierto = False
t = 0.0

# Ángulos
ang1 = -45   # Cerrado
ang2 = 45    # Abierto

def main():
    global t, abierto

    b = Button(19, pull_up=True)  # Botón en GPIO19

    factory = PiGPIOFactory()  # Para evitar jitter en el servo
    s = AngularServo(
        14,
        min_pulse_width=0.0005,
        max_pulse_width=0.0025,
        min_angle=-90,
        max_angle=90,
        pin_factory=factory
    )

    def cerrar():
        global t, abierto
        s.angle = ang1
        abierto = False
        t = time.time()

    def abrir():
        global t, abierto
        s.angle = ang2
        abierto = True
        t = time.time()

    def cambiar_orientacion():
        global abierto
        abierto = not abierto

        if abierto:
            abrir()
        else:
            cerrar()

    cerrar()  # Empezar cerrada
    b.when_pressed = cambiar_orientacion

    while True:
        if abierto and (time.time() - t) >= 10:
            cerrar()
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass