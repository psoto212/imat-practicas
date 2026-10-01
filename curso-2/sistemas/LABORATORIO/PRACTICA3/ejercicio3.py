from gpiozero import LEDBoard, Button
from time import sleep

def main():
    leds = LEDBoard(20, 21, 22, 23, 24, 25, 26, 27)

    boton_suma  = Button(19,  pull_up=True)  
    boton_resta = Button(16, pull_up=True)
    boton_reset = Button(17, pull_up=True)

    contador = {"val": 0}

    def mostrar():
        bits = [(contador["val"] >> bit) & 1 for bit in range(8)]
        leds.value = bits
        print("contador =", contador["val"], "bits =", bits)

    def sumar():
        contador["val"] = (contador["val"] + 1) & 0xFF
        print("SUMA (GPIO7)")
        mostrar()

    def restar():
        contador["val"] = (contador["val"] - 1) & 0xFF
        print("RESTA (GPIO16)")
        mostrar()

    def reset():
        contador["val"] = 0
        print("RESET (GPIO17)")
        mostrar()

    boton_suma.when_pressed = sumar
    boton_resta.when_pressed = restar
    boton_reset.when_pressed = reset

    mostrar()

    while True:
        sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")
