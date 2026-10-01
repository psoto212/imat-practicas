# ej1
from gpiozero import Button, LED, LEDBoard, PWMLED, MCP3008
from signal import pause
import time

def main():
    periodo = 0.05  
    puls = Button(16) 
    estado = ["APAGADA", "PARPADEO_1_HZ", "PARPADEO_2_HZ"]
    contador = 0  
    print(f"El estado es {estado[contador]}")
    def transicion():
        nonlocal contador
        contador = (contador + 1) % len(estado) 
        print(f"El estado es {estado[contador]}")
    puls.when_pressed = transicion  
    while True:
        time.sleep(periodo)

# ej2
def main2():
    periodo = 0.05  
    puls = Button(16)
    led = PWMLED(20) 
    estado = ["APAGADA", "PARPADEO_1_HZ", "PARPADEO_2_HZ"]
    contador = 0  
    print(f"El estado es {estado[contador]}")
    def transicion():
        nonlocal contador
        contador = (contador + 1) % len(estado) 
        print(f"El estado es {estado[contador]}")
    puls.when_pressed = transicion  
    ini = time.time()
    while True:
        fin = time.time()
        tiempo = fin-ini
        if tiempo >= periodo:
            ini = time.time()
            if contador == 1:
                led.frequency = 1
                led.duty_circle = 0.5
            elif contador == 2:
                led.frequency = 2
                led.duty_circle = 0.5
            elif contador == 0:
                led.off()

def main3():
    sensor = MCP3008(channel=7) 
    periodo = 0.05  
    puls = Button(16)
    led = PWMLED(20) 
    estado = ["APAGADA", "PARPADEO_1_HZ", "PARPADEO_2_HZ"]
    contador = 0 

    print(f"El estado es {estado[contador]}")
    def transicion():
        nonlocal contador 
        contador = (contador + 1) % len(estado) 
        print(f"El estado es {estado[contador]}")

    puls.when_pressed = transicion  
    ini = time.time()
    while True:
        fin = time.time()
        tiempo = fin-ini
        voltios = sensor.voltage
        lux = (voltios / 3.0) * 1500 # regla de 3
        if tiempo >= periodo:
            ini = time.time()
            # 0V --> 0lx y 3V --> 1500lx; 1000lx --> 2V
            if contador != 0 and lux < 1000: 
                led.value = 1
            else:
                if contador == 1:
                    led.frequency = 1
                    led.duty_cycle = 0.5
                elif contador == 2:
                    led.frequency = 2
                    led.duty_cycle = 0.5
                elif contador == 0:
                    led.off()
