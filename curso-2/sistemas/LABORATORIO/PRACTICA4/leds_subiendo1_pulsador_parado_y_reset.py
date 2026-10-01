from gpiozero import PWMLED, Button
from threading import Timer
from signal import pause

def main():
    leds = [PWMLED(pin, frequency=100) for pin in (20, 21, 22, 23)]

    boton_pausa = Button(19, pull_up=True)
    boton_reset = Button(17, pull_up=True)

    estado = {
        "brillo": 0.0,
        "paso": 0.25,
        "parado": False,
        "timer": None
    }

    def mostrar_brillo():
        for led in leds:
            led.value = estado["brillo"]

    def programar_siguiente():
        estado["timer"] = Timer(0.5, actualizar_brillo)
        estado["timer"].start()

    def actualizar_brillo():
        if not estado["parado"]:
            estado["brillo"] += estado["paso"]
            if estado["brillo"] > 1.0:
                estado["brillo"] = 0.0
            mostrar_brillo()

        programar_siguiente()

    def pausar_reanudar():
        estado["parado"] = not estado["parado"]

    def resetear():
        if estado["timer"] is not None:
            estado["timer"].cancel()

        estado["brillo"] = 0.0
        estado["parado"] = False
        mostrar_brillo()
        programar_siguiente()

    mostrar_brillo()

    boton_pausa.when_pressed = pausar_reanudar
    boton_reset.when_pressed = resetear

    programar_siguiente()
    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")