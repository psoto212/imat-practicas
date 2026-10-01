from gpiozero import LED,PWMLED, MCP3008
import time

def main():
    led_abajo = LED(20)
    led_arriba = LED(21)
    while True:
        sensor = MCP3008(channel=7)
        voltios = sensor.voltage
        print(voltios)
        if voltios < 1.65:
            led_abajo.on()
            led_arriba.off()
        else:
            led_arriba.on()
            led_abajo.off()

if _name_ == "_main_":
    try:
        main()
    except KeyboardInterrupt:
        pass