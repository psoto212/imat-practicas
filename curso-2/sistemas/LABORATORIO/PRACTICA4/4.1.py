from gpiozero import LED
from time import sleep



def main():
    led = LED(20)
    
    while True:
        led.toggle()
        sleep(0.2)
    

if __name__ == "__main__":
    try:
        main ()
    except KeyboardInterrupt:
        pass
