from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

def main():
    factory = PiGPIOFactory()

    servo = AngularServo(
        14,
        min_pulse_width=0.0005,
        max_pulse_width=0.0025,
        min_angle=-90,
        max_angle=90,
        pin_factory=factory
    )

    boton_toggle = Button(19, pull_up=True)
    boton_emergencia = Button(17, pull_up=True)

    CERRADO = -45
    ABIERTO = 45

    estado = {"abierto": False}

    def cerrar():
        servo.angle = CERRADO
        estado["abierto"] = False

    def abrir():
        servo.angle = ABIERTO
        estado["abierto"] = True

    def alternar():
        if estado["abierto"]:
            cerrar()
        else:
            abrir()

    def cierre_emergencia():
        cerrar()

    cerrar()
    boton_toggle.when_pressed = alternar
    boton_emergencia.when_pressed = cierre_emergencia

    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass