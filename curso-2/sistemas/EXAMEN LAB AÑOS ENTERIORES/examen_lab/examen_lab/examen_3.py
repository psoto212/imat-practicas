from gpiozero import AngularServo,Servo,Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import threading
from gpiozero import Button, LED, PWMLED
from signal import pause

def apertura():
    global ok
    print("esperar a que se abra")
    time.sleep(2)
    miservo.angle = 75 # aqui se abre 
    for led in leds_rojo:
        led.off()
    for led in leds_verdes:
        led.on()
    print("aviso de apertura")
    time.sleep(2)
    ok = True
    cierre()
    
def barrera():
    global ok
    if ok:
        ok = False
        apertura()
        
    else:
        ok = True

def cierre():
    miservo.angle = -15  # aqui se cierra
    for led in leds_verdes:
        led.off()
    for led in leds_rojo:
        led.on()

leds_rojo = [ LED(26), LED(27)]
led_naranja = LED(25)
leds_verdes = [ LED(23), LED(24)]
boton16 = Button(16)
boton17 = Button(17)
boton19 = Button(19)
ok = True


factory = PiGPIOFactory()
miservo = AngularServo(14, min_pulse_width = 0.5e-3, max_pulse_width = 2.5e-3, pin_factory=factory)

def main():
    while True:
        if boton16.is_pressed:
            led_naranja.off()
        else:
            led_naranja.on()
            time.sleep(0.5)
            led_naranja.off()
            time.sleep(0.5)

        boton19.when_pressed = barrera
        boton17.when_pressed = cierre


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        miservo.detach()
        pass