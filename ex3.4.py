import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            self.lock()
            if (self.head == 0 and self.tail == self.size - 1) or (self.tail == (self.head - 1) % (self.size - 1)):
                self.unlock()
                time.sleep(1)
            else:
                if self.head == -1:
                    self.head = self.tail = 0
                    self.queue[self.tail] = data
                else:
                    if self.tail == self.size - 1 and self.head != 0:
                        self.tail = 0
                    else:
                        self.tail += 1
                    self.queue[self.tail] = data
                self.unlock()
                return
    
    def dequeue(self):
        while True:
            self.lock()
            if self.head == -1:
                self.unlock()
                time.sleep(1)
            else:
                data = self.queue[self.head]
                self.queue[self.head] = None
                if self.head == self.tail:
                    self.head = self.tail = -1
                elif self.head == self.size - 1:
                    self.head = 0
                else:
                    self.head += 1
                self.unlock()
                return data
def producer():
    while True:
        data = random.randint(1,10)
        time.sleep(data)
        q.enqueue(data)

def consumer():
    while True:
       data = random.randint(1,10)
       time.sleep(data)
       print(q.dequeue())

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()