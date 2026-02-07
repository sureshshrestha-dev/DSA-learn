import threading
import time

class ThreadSafeCircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def put(self, item):
        with self.not_full:
            while self.count == self.size:
                self.not_full.wait()
            self.buffer[self.tail] = item
            self.tail = (self.tail + 1) % self.size
            self.count += 1
            self.not_empty.notify_all()

    def get(self):
        with self.not_empty:
            while self.count == 0:
                self.not_empty.wait()
            item = self.buffer[self.head]
            self.head = (self.head + 1) % self.size
            self.count -= 1
            self.not_full.notify_all()
            return item

def producer(buffer):
    for i in range(10):
        print(f"Producing {i}")
        buffer.put(i)
        time.sleep(0.1)

def consumer(buffer):
    for _ in range(10):
        item = buffer.get()
        print(f"Consuming {item}")
        time.sleep(0.2)

if __name__ == "__main__":
    buf = ThreadSafeCircularBuffer(5)
    t1 = threading.Thread(target=producer, args=(buf,))
    t2 = threading.Thread(target=consumer, args=(buf,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("Thread-safe Circular Buffer simulation complete.")
