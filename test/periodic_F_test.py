import threading
from time import sleep

class AsyncTask:
    def __init__(self):
        pass

    def TaskA(self):
        print('Process A')
        threading.Timer(1,self.TaskA).start()

    def TaskB(self):
        print ('Process B')
        threading.Timer(3, self.TaskB).start()

def counting_complete():
    pass

def main():
    print ('Async Function')
    at = AsyncTask()
    at.TaskA()
    at.TaskB()
    for i in range(10):
        print("sleep count : ", i)
        sleep(1)
    counting_complete()

if __name__ == '__main__':
    main()
