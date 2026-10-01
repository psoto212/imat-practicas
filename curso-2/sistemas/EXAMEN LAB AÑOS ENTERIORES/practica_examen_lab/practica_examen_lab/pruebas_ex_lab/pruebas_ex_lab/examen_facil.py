# ej 1
from gpiozero import Button, LEDBoard, PWMLED, MCP3008
import time
def main1():
    puls = Button(7)
    leds_pulsar = LEDBoard(22,23,24,25)
    leds_soltar = LEDBoard(20,21,26,27)
    while True:
        if puls.is_pressed:
            leds_pulsar.on()
            leds_soltar.off()
        else:
            leds_pulsar.off()
            leds_soltar.on()

# ej2, COMPROBAR EN EL OSCILOSCOPIO!!!!!
def main2():
    puls = Button(7)
    leds_pulsar = LEDBoard(PWMLED(22), PWMLED(23), PWMLED(24), PWMLED(25))
    leds_soltar = LEDBoard(PWMLED(20), PWMLED(21), PWMLED(26), PWMLED(27))

    while True:
        if puls.is_pressed:
            leds_pulsar.blink(0.5,0.5)
            leds_soltar.off()
        else:
            leds_pulsar.off()
            leds_soltar.blink(0.25,0.25)

# ej3
def main3():
    sensor = MCP3008(channel=7) 
    # si la R = 1ko, vo = 3.3*(1/2)
    v0_1 = 3.3*(1/2)
    # si la R = 1ko, vo = 3.3*(1/2)
    v0_4_7 = 3.3*(4.7/5.7)
    leds_pulsar = LEDBoard(PWMLED(22), PWMLED(23), PWMLED(24), PWMLED(25))
    leds_soltar = LEDBoard(PWMLED(20), PWMLED(21), PWMLED(26), PWMLED(27))

    while True:
        # Le añades una tolerancia a la medida del voltaje
        # nunca van a coincidir los dos elifs ya que su ditancia es de mas de 0.1
        voltios = sensor.voltage
        if abs(voltios - v0_1) < 0.05:  
            leds_pulsar.blink(0.5, 0.5)  
            leds_soltar.off()
        elif abs(voltios - v0_4_7) < 0.05: 
            leds_pulsar.off()
            leds_soltar.blink(0.25, 0.25)  
        else:
            leds_pulsar.off()
            leds_soltar.off()
        

if __name__ == "__main__":
    try:
        main1()
    except KeyboardInterrupt:
        pass
