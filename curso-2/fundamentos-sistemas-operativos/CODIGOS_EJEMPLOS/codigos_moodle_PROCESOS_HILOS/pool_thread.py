from multiprocessing.pool import ThreadPool
import time
import random

init = 1
def thread_task(idx: int):
    global init
    for i in range(0, 10):
        time.sleep(random.uniform(0, 1))        
        print(f"Thread {idx}. It. {i}, value {init}")
        init += 1

if __name__ == "__main__":  
    idxs = [0, 1]
    p = ThreadPool(2)
    p.map(thread_task, idxs)
    p.close() # No more tasks can be sent to the Process Pool
    p.join() # Wait all pool workers to finish
    print("All finished")