from multiprocessing import Process
import time
import random

init = 1
def process_task(idx: int):
    global init
    for i in range(0, 10):
        time.sleep(random.uniform(0, 1))
        print(f"Process {idx}. It. {i}, value {init}")
        init += 1

if __name__ == "__main__":  
    proc1 = Process(target=process_task, args=(0,))  
    proc1.start()

    proc2 = Process(target=process_task, args=(1,))  
    proc2.start()
    print("hola")
    proc1.join()  # Join blocks the parent process until its child has finished. That is, it does not advance until proc1's code has finished.
    print("adios")
    proc2.join()  # Same functionality as above but with proc 2.
    
    # Why doesn't the init variable change between processes? -> Each process has a completely independent memory area.