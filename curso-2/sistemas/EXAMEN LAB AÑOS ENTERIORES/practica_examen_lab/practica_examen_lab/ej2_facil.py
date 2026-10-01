from gpiozero import Button, LEDBoard
from signal import pause

# Configuración de pines
boton = Button(7)
leds_centrales = LEDBoard(22, 23, 24, 25)
leds_externos = LEDBoard(20, 21, 26, 27)

# Función cuando el botón está presionado
def cuando_presionado():
    leds_externos.off()
    leds_centrales.blink(on_time=0.5, off_time=0.5)

#esta funcion lo que hace es mantenerlos encendidos este tiempo
# si te dicen 1 hz es 0.5 y 2hz es 0.25, calculos en la practica 3 ejerciio 2

# Función cuando el botón no está presionado
def cuando_suelto():
    leds_centrales.off()
    leds_externos.blink(on_time=0.25, off_time=0.25)

# Asignar funciones a eventos del botón
boton.when_pressed = cuando_presionado
boton.when_released = cuando_suelto

# Mantener el script en ejecución
pause()
