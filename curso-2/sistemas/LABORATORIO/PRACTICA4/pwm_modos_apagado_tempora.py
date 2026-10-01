from gpiozero import PWMLED, Button
from threading import Timer
from signal import pause

def main():
    leds = [PWMLED(pin, frequency=100) for pin in (20, 21, 22, 23)]

    boton_cambio = Button(19, pull_up=True)
    boton_apagado = Button(17, pull_up=True)

    estado = {
        "brillo": 0.0,
        "paso": 0.25,
        "ascendente": True,
        "apagado_temporal": False,
        "timer": None
    }

    def mostrar_brillo():
        for led in leds:
            led.value = estado["brillo"]

    def programar_siguiente():
        estado["timer"] = Timer(0.5, actualizar_brillo)
        estado["timer"].start()

    def actualizar_brillo():
        if not estado["apagado_temporal"]:
            if estado["ascendente"]:
                estado["brillo"] += estado["paso"]
                if estado["brillo"] > 1.0:
                    estado["brillo"] = 0.0
            else:
                estado["brillo"] -= estado["paso"]
                if estado["brillo"] < 0.0:
                    estado["brillo"] = 1.0

            mostrar_brillo()

        programar_siguiente()

    def cambiar_modo():
        estado["ascendente"] = not estado["ascendente"]

    def reanudar():
        estado["apagado_temporal"] = False
        estado["brillo"] = estado["brillo_guardado"]
        mostrar_brillo()
        programar_siguiente()

    def apagar_temporalmente():
        if estado["timer"] is not None:
            estado["timer"].cancel()

        estado["brillo_guardado"] = estado["brillo"]
        estado["apagado_temporal"] = True

        for led in leds:
            led.off()

        Timer(2.0, reanudar).start()

    mostrar_brillo()

    boton_cambio.when_pressed = cambiar_modo
    boton_apagado.when_pressed = apagar_temporalmente

    programar_siguiente()
    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")