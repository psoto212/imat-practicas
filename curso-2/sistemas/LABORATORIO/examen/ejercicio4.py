from gpiozero import PWMLED, Button
from threading import Timer,Event

def main():
    Led = PWMLED(26,frequency = 5)
    Led.value = 0.4
    Led.on()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")
