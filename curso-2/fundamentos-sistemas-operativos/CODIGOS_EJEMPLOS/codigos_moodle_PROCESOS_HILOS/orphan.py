from multiprocessing import Process
import time, sys

def level_1():
    print("I am the child")
    process = Process(target=level_2)
    process.start()
    time.sleep(20)
    print("I am the child and I finish")

def level_2():
    print("I am the grandchild")
    time.sleep(20)
    print("I am the grandchild and I finish")

if __name__ == '__main__':    
    process = Process(target=level_1)
    process.start()
    print("I kill the child process and I finish")
    time.sleep(10)
    process.terminate()