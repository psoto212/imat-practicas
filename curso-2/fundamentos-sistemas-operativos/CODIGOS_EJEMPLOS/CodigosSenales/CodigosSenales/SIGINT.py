import signal, os
import time

contador_senal = 0
def handler(sig_num, curr_stack_frame):
    global contador_senal
    print(f"Recibida la senal SIGINT")
    contador_senal += 1

if __name__ == "__main__":
	# Registramos SIGINT para que ejecute la funcion handler
    signal.signal(signal.SIGINT, handler)
    
    for i in range(50):
        time.sleep(1)
        print(f"{i} Llevamos {contador_senal}. Mi id es {os.getpid()}")