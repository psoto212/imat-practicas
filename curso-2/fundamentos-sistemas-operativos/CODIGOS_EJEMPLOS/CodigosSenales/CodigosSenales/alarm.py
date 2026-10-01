import signal
import time


def handler(sig_num, curr_stack_frame):
    print(f"Recibida la senal  {signal.strsignal(sig_num)}")

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)
    # Despues de 3 segundos se envia la alarma 
    signal.alarm(3)
    print("Enviamos la alarma en 3 segundos")
    time.sleep(6)
    # Despues de 3 segundos se envia la alarma
    signal.alarm(3)
    print("Enviamos la alarma en 3 segundos")
    time.sleep(6)
