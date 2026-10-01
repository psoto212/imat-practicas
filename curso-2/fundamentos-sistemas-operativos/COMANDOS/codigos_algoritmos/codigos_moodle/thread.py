from threading import Thread
import time
import random

init = 1
def thread_task(idx: int):
    global init # Its a global variable, so init is shared between threads in a process
    a = 0
    for i in range(0, 10):
        time.sleep(random.uniform(0, 1))
        print(f"Thread {idx}. It. {i}, value {init}")
        init += 1
        a = a + 1
    print(a)
        
if __name__ == "__main__":  
    th1 = Thread(target=thread_task, args=(0,))  
    th1.start()

    th2 = Thread(target=thread_task, args=(1,))  
    th2.start()

    th1.join() # Same operation of the join, as in the example of the processes
    th2.join()