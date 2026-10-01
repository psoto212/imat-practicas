from gpiozero import LED
from time import sleep
import os

# Definir los pines de los LEDs (20-27)
led_pins = list(range(20, 28))  # LEDs en pines 20-27
leds = [LED(pin) for pin in led_pins]

def limpiar_gpio():
    """Limpia los pines GPIO y reinicia el script."""
    print("¡GPIO ocupado! Limpiando...")
    os.system("gpio unexportall")  # Libera todos los pines ocupados
    sleep(0.5)  # Esperar un poco antes de reconfigurar
    global leds
    leds = [LED(pin) for pin in led_pins]  # Reconfigurar LEDs
    print("GPIO limpio y LEDs restablecidos.")

try:
    while True:
        try:
            # Encender y apagar los LEDs
            for led in leds:
                led.on()
            sleep(1)
            for led in leds:
                led.off()
            sleep(1)

        except OSError as e:
            if "Device or resource busy" in str(e):
                limpiar_gpio()
            else:
                print(f"Error inesperado: {e}")
                break

except KeyboardInterrupt:
    print("Saliendo...")

finally:
    for led in leds:
        led.close()  # Apagar y liberar los LEDs
    print("GPIO limpio y programa terminado.")

