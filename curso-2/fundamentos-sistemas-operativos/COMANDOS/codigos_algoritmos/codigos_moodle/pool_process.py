from multiprocessing import Pool
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
    idxs = [0, 1]
    p = Pool(2)
    p.map(process_task, idxs) 
    p.close() # No more tasks can be sent to the Process Pool
    p.join() # Wait all pool workers to finish
    print("All finished")