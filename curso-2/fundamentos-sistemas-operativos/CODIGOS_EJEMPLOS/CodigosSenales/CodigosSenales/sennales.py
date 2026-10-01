import os, time, signal
from multiprocessing import Process

def manejador(sig_num, curr_stack_frame):
    print(f'Soy {os.getpid()}. He recibido SIGINT')

def proceso():
    signal.signal(signal.SIGINT, manejador)
    for i in range (10):
        time.sleep(1)
        os.kill(os.getppid(), signal.SIGINT)

if __name__ == "__main__":
    ind_process = Process(target = proceso)
    ind_process.start()
    signal.signal(signal.SIGINT, manejador)
    for i in range (10):
        time.sleep(1)
        os.kill(ind_process.pid, signal.SIGINT)
    ind_process.join()
